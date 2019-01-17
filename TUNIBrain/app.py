from gevent import monkey; monkey.patch_all()

from bottle import Bottle, run, \
template, debug, static_file, request, post, get, route, hook, response

import os, sys
import requests
import json
import socket

from inspect import getsourcefile
from os.path import abspath
from parse_uta_databank import UTAJsonParser
from TAMK_API_implementations import *
from TAMK_API_courseunits import *

from Log import Logger

import re

dirname = os.path.dirname(abspath(getsourcefile(lambda:0)))

app = Bottle()
#debug(True)

# enable or disable logging
logs_on = False

RASA_ADDRESS = "http://localhost:5000/parse" # http address of rasa server
RASA_THRESHOLD = 1.1 # confidence threshold for using rasa response (when no entities are detected)
# RASA_THRESHOLD is never achieved (max is 1.0), effectively switched off when no entities detected
RASA_THRESHOLD_DEFAULTINFO = 0.90 # confidence threshold for using rasa response (when no entities are detected)
RASA_THRESHOLD_DEFAULTINFO_ENTITY = 0.90
RASA_SPECIAL = 0.25 # confidence threshold for using rasa response (when entities are detected)
RASA_SPECIAL_ENTITY = 0.35 # entity confidence threshold for using rasa response (when entities are detected)
UTA_PARSER = UTAJsonParser("jsons") # initialize uta parser with jsons directory
PROGRAMY_ENDPOINT = "http://localhost:8989/api/rest/v1.0/ask?question=*1&userid=*2"

# add cors header to all requests
@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

# return files from the static path
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

logger = Logger(logs_on)

# note: comments in Finnish
def query_chatscript(query, userID="TestUser"):
    # Lokaalin testiympäristön osoite. Muistetaan muokata, kunhan CS
    # on serverillä.
    addr = ("localhost", 1024)

    # UserID pitäisi lopulta tulla ulkopuolelta, tässä koodissa se on
    # väliaikaisen tekstikäytön vuoksi stdin.

    # Tällä hetkellä skripti yhdistää oletusbottiin. Pitää muokata, jos
    # lopulta serverillä on jostain syystä useampi CS-botti.
    bot = ''
    # data_iniin pitää muokata CS-botille lähetettävä kysymys.
    data_in = query

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    client_socket.sendall((userID+chr(0)+bot+chr(0)+data_in+chr(0)).encode('utf-8'))

    # data_out on CS-botin vastaus lähetettyyn kysymykseen. Se pitäisi siis
    # lähettää jonnekin eteenpäin.
    data_out = client_socket.recv(1000)
    client_socket.close()

    return data_out.decode("utf-8")

# parse rasa json and respond with appropriate response from tamk or uta (tuni) backends
# needs major refactoring
def parse_rasa_json(receivedThreshold, rasa_json):
    response = ""
    try:
        if receivedThreshold > RASA_THRESHOLD or (receivedThreshold > RASA_SPECIAL and \
        "entities" in rasa_json and len(rasa_json['entities']) > 0 and \
        rasa_json['entities'][0]['confidence'] > RASA_SPECIAL_ENTITY):
            if rasa_json['intent']['name'] == 'startDate': # check intent name
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        # if course found, search for course and add to response
                        # all of the following intents follow this basic pattern
                        uta = UTA_PARSER.find_course_start_date(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_startDate(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_start_date(name=coursename)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_startDate(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                else:
                    response = "Are you asking for course starting dates?\nYou need to mention a course code/name to help me search."
            if rasa_json['intent']['name'] == 'kieli':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teachinglanguage(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_teachingLanguage(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teachinglanguage(name=coursename)

                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_teachingLanguage(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                else:
                    response = "Are you asking for course teaching language?\nYou need to mention a course code/name to help me search."
            if rasa_json['intent']['name'] == 'opetusajat' or \
                        rasa_json['intent']['name'] == 'periodi':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teaching_times(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_examSchedule(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teaching_times(name=coursename)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_examSchedule(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                else:
                    response = "Are you asking for course schedules?\nYou need to mention a course code/name to help me search."

            if rasa_json['intent']['name'] == 'poikkeusajat':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_deviations(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_deviations(name=coursename)
                        if len(uta) > 2:
                            response = uta
                else:
                    response = "Are you asking for exceptions in the course schedule?\nYou need to mention a course code/name to help me search."

            if rasa_json['intent']['name'] == 'creditsMin':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_credits(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_credits(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_credits(name=coursename)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_credits(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                else:
                    response = "Are you asking for course credits?\nYou need to mention a course code/name to help me search."
            if rasa_json['intent']['name'] == 'nimi':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_name(coursecode)
                        if uta is not None and len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_course_name(id=coursecode)
                            if tamk is not None and len(tamk) > 2:
                                response += tamk
                            else:
                                tamk2 = tamk_course_name_fromunit(id=coursecode)
                                if tamk2 is not None and len(tamk2) > 2:
                                    response += tamk2
                else:
                    response = "Are you asking for course name?\nYou need to mention a course code to help me search."

            if rasa_json['intent']['name'] == 'paikka':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teaching_times(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_location(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teaching_times(name=coursename)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_location(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                else:
                    response = "Are you asking for course location?\nYou need to mention a course code/name to help me search."

            if rasa_json['intent']['name'] == 'defaultinfo' and \
            (receivedThreshold > RASA_THRESHOLD_DEFAULTINFO and \
            "entities" in rasa_json and len(rasa_json['entities']) > 0 and \
            rasa_json['entities'][0]['confidence'] > RASA_THRESHOLD_DEFAULTINFO_ENTITY): # check intent name, special
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        # return start date and language if asking generic question about course
                        uta = UTA_PARSER.find_course_start_date(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_startDate(id=coursecode)
                            if len(tamk) > 2:
                                response += tamk
                        uta = UTA_PARSER.find_course_teachinglanguage(id=coursecode)
                        if len(uta) > 2:
                            response += "\n" + uta
                        else:
                            tamk = tamk_teachingLanguage(id=coursecode)
                            if len(tamk) > 2:
                                response += "\n" + tamk
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_start_date(name=coursename)
                        if len(uta) > 2:
                            response = uta
                        else:
                            tamk = tamk_startDate(name=coursename)
                            if len(tamk) > 2:
                                response += tamk
                        uta = UTA_PARSER.find_course_teachinglanguage(name=coursename)
                        if len(uta) > 2:
                            response += "\n" + uta
                        else:
                            tamk = tamk_teachingLanguage(id=coursename)
                            if len(tamk) > 2:
                                response += "\n" + tamk


    except Exception as e:
        print("Error in rasa code:")
        traceback.print_exc()

    # if response is too short (empty), set response to None in order to use ChatScript or rosie response
    if response is not None and len(response) < 3:
        response = None

    return response

@app.route('/msg', method='POST')
def test():
    username = request.forms.username #+ ":tunibottitoo"
    if username is None:
        username = "TestUser"
    print("Username: " + username)

    query = request.forms.query
    print("query: " + query)

    #Removes special characters from query, and makes it start with uppercase letter
    cleaning_query = ''.join(e for e in query if e.isalnum() or e.isspace() or e == '-')
    cleaned_query = "".join(c.upper() if i is 0 else c for i, c in enumerate(cleaning_query))

    # send user query to rasa, utf-8 encoding
    rasa_query = '{"query":"' + cleaned_query + '", "project": "current"}'
    rasa_response = requests.post(RASA_ADDRESS, data=rasa_query.encode("utf-8"))
    rasa_response.encoding = "utf-8"
    #print(rasa_response.text)

    rasa_json = json.loads(rasa_response.text, encoding="utf-8")
    print(rasa_json)
    receivedThreshold = rasa_json['intent']['confidence']
    print("rasa conf " + "{0:.2f}".format(receivedThreshold))
    need_cs_response = True
    response = parse_rasa_json(receivedThreshold, rasa_json)
    success = True

    # if parsing rasa json succeeded, we don't need a chatscript response
    if response is not None:
        need_cs_response = False

    # otherwise, send user query to chatscript bot
    if need_cs_response:
        response = query_chatscript(query, userID=username)
        print("Chatscript response: " + response)

    # was ChatScript able to answer?
    # should switch this phrase to something more distinct
    if need_cs_response and "Please ask me anything you" in response:
        print("did not succeed at rasa or chatscript")
        success = False

    # if Rasa and ChatScript were not able to respond
    # rosie (program-y) is the final
    if not success:
        print("trying program-y")
        try:
            aiml_response = requests.get(PROGRAMY_ENDPOINT.replace("*1",query)\
            .replace("*2",username).encode("ISO 8859-1"))
            aiml_response.encoding = "ISO 8859-1"
            aiml_json = json.loads(aiml_response.text)
            response = aiml_json[0]['response']['answer']
            Source = "Program-Y"
        except Exception as e:
            print("aiml failed: " + str(e))

    #Logs
    if logs_on:
        if need_cs_response:
            Source = 'Chatscript'
            receivedThreshold = 0
            if not success:
                Source = 'Program-Y'
        else:
            Source = 'Rasa'

        #Was the answer successful or not
        if receivedThreshold <= 0:
            if success:
                logger.log_success(query, response, 0, "none", 0, "none", Source)
            else:
                logger.log_failed(query, response, 0, "none", 0, "none", Source)
        elif len(rasa_json["entities"]) == 0:
            if success:
                logger.log_success(query, response, rasa_json['intent']['confidence'],\
                rasa_json['intent']['name'], 0, "none", Source)
            else:
                logger.log_failed(query, response, rasa_json['intent']['confidence'],\
                rasa_json['intent']['name'], 0, "none", Source)
        else:
            if success:
                logger.log_success(query, response, rasa_json['intent']['confidence'],\
                 rasa_json['intent']['name'], rasa_json["entities"][0]["confidence"],\
                 rasa_json["entities"][0]["entity"], Source)
            else:
                logger.log_failed(query, response, rasa_json['intent']['confidence'],\
                rasa_json['intent']['name'], rasa_json["entities"][0]["confidence"],\
                rasa_json["entities"][0]["entity"], Source)


    header = "<html><body>"

    footer = "</body></html>"

    #replace("\n", "\r\n").replace("  ", "&nbsp&nbsp")

    # return bot response, replacing incorrectly formatted newlines
    return header + response.replace("\\r\\n", "\r\n").replace("\\n", "\r\n")\
    .replace("\\r", "\r\n").replace("\n", "\r\n").replace("\r\n", "\r\n") + footer



def main():
    run(app, host='localhost', port=8082)

if __name__ == "__main__":
    main()
