import requests, json
from datetime import datetime
import dateutil.parser

#Gets courses info from TAMK API by course id
def TAMK_API_implementations(id):
    try:
        #TAMK
        #URL and other info for API request
        url = 'https://opendata.tamk.fi/r1/realization/search'
        headers = {'Accept-Language':'en', 'content-type':'application/json'}
        info = {"codes": [id]}
        info = json.dumps(info)
        loaded_info = json.loads(info)

        #Makes API-request and returns data in json-form.
        r = requests.post(url, auth=('***REMOVED***', ''), data=info, headers=headers)
        ret = json.loads(r.text)
        return ret
    except Exception as e:
        print(e)

    return None

#Searches courses teaching language by its id
def TAMK_teachingLanguage(id):
    try:
        info = TAMK_API_implementations(id)
        language = info['realizations'][0]['teachingLanguage']
        if(language == 'en'):
            language = 'english'
        elif(language == 'fi'):
            language = 'finnish'
        elif(language == 'sv'):
            language = 'swedish'
        return("Teaching language of the course "+str(id)+" is "+language+".")
    except Exception as e:
        print(e)
    return ""

#print(TAMK_teachingLanguage("IM00BR45-3003"))

#Searches courses starting date by its id
def TAMK_startDate(id):
    try:
        info = TAMK_API_implementations(id)
        startDate = dateutil.parser.parse(info['realizations'][0]['startDate'])
        startDate = startDate.strftime('%d-%m-%Y')
        return("Starting date of the course "+str(id)+" is "+str(startDate)+".")
    except Exception as e:
        print(e)
    return ""

#print(TAMK_startDate("IM00BR45-3003"))

#Searches courses location by its id
def TAMK_location(id):
    try:
        info = TAMK_API_implementations(id)
        en_location = info['realizations'][0]['office']['localizedName']['en']
        fi_location = info['realizations'][0]['office']['localizedName']['fi']
        sv_location = info['realizations'][0]['office']['localizedName']['sv']
        if(en_location != ""):
            location = en_location
        elif(fi_location != ""):
            location = fi_location
        elif(sv_location != ""):
            location = sv_location
        return("Location of the course "+str(id)+" is "+location+"." )
    except Exception as e:
        print(e)

    return ""

#print(TAMK_location("IM00BR45-3003"))
