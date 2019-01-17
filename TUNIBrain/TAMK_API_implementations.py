import requests, json
from datetime import datetime
import dateutil.parser
import traceback

#Gets courses info from TAMK API by course id
def tamk_API_implementations(id=None, name=None):
    try:
        #TAMK
        #URL and other info for API request
        url = 'https://opendata.tamk.fi/r1/realization/search'
        headers = {'Accept-Language':'en', 'content-type':'application/json'}
        if id is not None:
            info = {"codes": [id]}
        elif name is not None:
            info = {"name": name}
        info = json.dumps(info)
        loaded_info = json.loads(info)

        #Makes API-request and returns data in json-form.
        r = requests.post(url, auth=('***REMOVED***', ''), data=info, headers=headers)
        ret = json.loads(r.text)
        return ret
    except Exception as e:
        traceback.print_exc()

    return None

#Searches course name by its id
def tamk_course_name(id=None):
    try:
        if id is not None:
            info = tamk_API_implementations(id=id)
        if id.lower() in info['realizations'][0]['code'].lower():
            name = info['realizations'][0]['name']
            return("Name of the course "+str(id)+" is "+name+".")
        else:
            return ""
    except Exception as e:
        traceback.print_exc()
    return ""

#Searches courses teaching language by its id
def tamk_teachingLanguage(id=None, name=None):
    try:
        if id is not None:
            info = tamk_API_implementations(id=id)
            if id.lower() not in info['realizations'][0]['code'].lower():
                return ""
            #print(info)
            #print("CODE")
        elif name is not None:
            info = tamk_API_implementations(name=name)
            if name.lower() not in info['realizations'][0]['name'].lower():
                return ""
            #print(info)
            #print("NAME")
        language = info['realizations'][0]['teachingLanguage']
        if(language == 'en'):
            language = 'english'
        elif(language == 'fi'):
            language = 'finnish'
        elif(language == 'sv'):
            language = 'swedish'
        return("Teaching language of the course "+info['realizations'][0]['name']+" is "+language+".")
    except Exception as e:
        traceback.print_exc()
    return ""



#Searches courses starting date by its id
def tamk_startDate(id=None, name=None):
    try:
        if id is not None:
            info = tamk_API_implementations(id=id)
            if id.lower() not in info['realizations'][0]['code'].lower():
                return ""
        elif name is not None:
            info = tamk_API_implementations(name=name)
            if name.lower() not in info['realizations'][0]['name'].lower():
                return ""
        startDate = dateutil.parser.parse(info['realizations'][0]['startDate'])
        startDate = startDate.strftime('%d-%m-%Y')
        return("Starting date of the course "+info['realizations'][0]['name']+" is "+str(startDate)+".")
    except Exception as e:
        traceback.print_exc()
    return ""



#Searches courses location by its id
def tamk_location(id=None, name=None):
    try:
        if id is not None:
            info = tamk_API_implementations(id=id)
            if id.lower() not in info['realizations'][0]['code'].lower():
                return ""
        elif name is not None:
            info = tamk_API_implementations(name=name)
            if name.lower() not in info['realizations'][0]['name'].lower():
                return ""
        en_location = info['realizations'][0]['office']['localizedName']['en']
        fi_location = info['realizations'][0]['office']['localizedName']['fi']
        sv_location = info['realizations'][0]['office']['localizedName']['sv']
        if(en_location != ""):
            location = en_location
        elif(fi_location != ""):
            location = fi_location
        elif(sv_location != ""):
            location = sv_location
        return("Location of the course "+info['realizations'][0]['name']+" is "+location+"." )
    except Exception as e:
        traceback.print_exc()

    return ""



#Searches courses exam dates by its id
def tamk_examSchedule(id=None, name=None):
    try:
        if id is not None:
            info = tamk_API_implementations(id=id)
            if id.lower() not in info['realizations'][0]['code'].lower():
                return ""
        elif name is not None:
            info = tamk_API_implementations(name=name)
            if name.lower() not in info['realizations'][0]['name'].lower():
                return ""
        exams = info['realizations'][0]['examSchedule']
        if exams is "":
            exams = "unknown"
        return("Exam schedule of the course "+info['realizations'][0]['name']+" is: "+exams)
    except Exception as e:
        traceback.print_exc()
    return""

#print(tamk_course_name("IM00BR45-3003"))
#print(tamk_teachingLanguage(name="Knowledge Management"))
#print(tamk_startDate("IM00BR45-3003"))
#print(tamk_location("IM00BR45-3003"))
#print(tamk_examSchedule("IM00BR45-3003"))
