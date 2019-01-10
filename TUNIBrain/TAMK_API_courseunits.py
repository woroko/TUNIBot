import requests, json
import traceback

#Gets courses info from TAMK API by course id
def tamk_API_courseunits(id=None, name=None):
    #TAMK
    #URL and other info for API request
    url = 'https://opendata.tamk.fi/r1/courseunit/search'
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

#Searches course name by its id
def tamk_course_name_fromunit(id=None):
    try:
        if id is not None:
            info = tamk_API_courseunits(id=id)
        name = info['courseUnits'][0]['name']
        print("unit info:")
        print(info)
        return("Name of the course "+str(id)+" is "+name+".")
    except Exception as e:
        pass
        #print("from courseunit error")
        #traceback.print_exc()

#Searches courses credits by its id
def tamk_credits(id=None, name=None):
    if(id is not None):
        info = tamk_API_courseunits(id=id)
    elif(name is not None):
        info = tamk_API_courseunits(name=name)
    credits = info['courseUnits'][0]['credits']
    return("Course "+ info['courseUnits'][0]['name'] +" is worth "+str(credits)+" credits.")
print(tamk_credits("IM00BR45"))
