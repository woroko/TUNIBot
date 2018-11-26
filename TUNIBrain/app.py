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

from Log import Logger

import re

dirname = os.path.dirname(abspath(getsourcefile(lambda:0)))

app = Bottle()
debug(True)
#Are logs working
logs_on = True

RASA_ADDRESS = "http://localhost:5000/parse"
RASA_THRESHOLD = 0.6
RASA_SPECIAL = 0.2
RASA_SPECIAL_ENTITY = 0.35
UTA_PARSER = UTAJsonParser("jsons")
PROGRAMY_ENDPOINT = "http://localhost:8989/api/rest/v1.0/ask?question=*1&userid=*2"


from gevent import monkey; monkey.patch_all()

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8082'

@app.route('/static/<filename>')
def server_static(filename):
    #return "hey"
    return static_file(filename, root='static')

logger = Logger(logs_on)

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
    data_out = client_socket.recv(200)
    client_socket.close()

    return data_out.decode("utf-8")

@app.get('/') # or @route('/login')
def login():
    return '''
        <form action="/msg" method="post">
            <input name="username" type="hidden" value="testUser" />
            Query: <input name="query" type="text" />
            <input value="Send" type="submit" />
        </form>
    '''

def parse_rasa_json(receivedThreshold, rasa_json):
    response = None
    try:
        if receivedThreshold > RASA_THRESHOLD or (receivedThreshold > RASA_SPECIAL and \
        "entities" in rasa_json and len(rasa_json['entities']) > 0 and \
        rasa_json['entities'][0]['confidence'] > RASA_SPECIAL_ENTITY):
            if rasa_json['intent']['name'] == 'startDate':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_start_date(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_start_date(name=coursename)
                        if len(uta) > 2:
                            response = uta
                else:
                    response = "Are you asking for course starting dates?\nYou need to mention a course code/name to help me search."
            if rasa_json['intent']['name'] == 'kieli':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teachinglanguage(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teachinglanguage(name=coursename)
                        if len(uta) > 2:
                            response = uta
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
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_teaching_times(name=coursename)
                        if len(uta) > 2:
                            response = uta
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
                    response = "Are you asking for course time exceptions?\nYou need to mention a course code/name to help me search."

            if rasa_json['intent']['name'] == 'creditsMin':
                if len(rasa_json["entities"]) > 0:
                    if rasa_json["entities"][0]["entity"] == "course":
                        coursecode = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_credits(id=coursecode)
                        if len(uta) > 2:
                            response = uta
                    elif rasa_json["entities"][0]["entity"] == "coursename":
                        coursename = rasa_json["entities"][0]['value']
                        uta = UTA_PARSER.find_course_credits(coursecode)
                        if len(uta) > 2:
                            response = uta
                else:
                    response = "Are you asking for course credits?\nYou need to mention a course code/name to help me search."

    except Exception as e:
        print("Error in rasa code:")
        print(e)

    return response

@app.route('/msg', method='POST')
def test():
    username = request.forms.get('username') #+ ":tunibottitoo"
    if username is None:
        username = "TestUser"
    print("Username: " + username)

    query = request.forms.get('query')

    #Are logs working
    logs_on = False
    #Removes special characters from query, and makes it start with uppercase letter
    cleaning_query = ''.join(e for e in query if e.isalnum() or e.isspace())
    cleaned_query = "".join(c.upper() if i is 0 else c for i, c in enumerate(cleaning_query))


    #response = requests.get("api-address")
    #response = '{"intent": {"confidence": 0.5}}'
    rasa_query = '{"query":"' + cleaned_query + '", "project": "current"}'
    rasa_response = requests.post(RASA_ADDRESS, data=rasa_query)
    rasa_json = json.loads(rasa_response.text)
    #print(rasa_json)
    receivedThreshold = rasa_json['intent']['confidence']
    print("rasa conf " + "{0:.2f}".format(receivedThreshold))
    need_cs_response = True
    response = parse_rasa_json(receivedThreshold, rasa_json)
    success = True

    if response is not None:
        need_cs_response = False

    if need_cs_response:
        response = query_chatscript(query, userID=username)
        print("Chatscript response: " + response)

    #Was ChatScript able to answer?
    if need_cs_response and \
    "Please ask me anything you" in response:
        print("did not succeed at rasa or chatscript")
        success = False

    if not success:
        print("trying program-y")
        try:
            aiml_response = requests.get(PROGRAMY_ENDPOINT.replace("*1",query)\
            .replace("*2",username))
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
                logger.log_success(query, response, rasa_json['intent']['confidence'], rasa_json['intent']['name'], 0, "none", Source)
            else:
                logger.log_failed(query, response, rasa_json['intent']['confidence'], rasa_json['intent']['name'], 0, "none", Source)
        else:
            if success:
                logger.log_success(query, response, rasa_json['intent']['confidence'], rasa_json['intent']['name'], rasa_json["entities"][0]["confidence"], rasa_json["entities"][0]["entity"], Source)
            else:
                logger.log_failed(query, response, rasa_json['intent']['confidence'], rasa_json['intent']['name'], rasa_json["entities"][0]["confidence"], rasa_json["entities"][0]["entity"], Source)


    header = "<html><body>"

    footer = "</body></html>"

    #replace("\n", "<br>").replace("  ", "&nbsp&nbsp")
    return header + response + footer



def main():
    run(app, host='localhost', port=8082)

if __name__ == "__main__":
    main()
