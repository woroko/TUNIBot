import requests, json

#Gets courses info from TAMK API by course id
def tamk_API_courseunits(id):
   #TAMK 
   #URL and other info for API request
   url = 'https://opendata.tamk.fi/r1/courseunit/search'
   headers = {'Accept-Language':'en', 'content-type':'application/json'}
   info = {"codes": [id]}
   info = json.dumps(info)
   loaded_info = json.loads(info)
   
   #Makes API-request and returns data in json-form.
   r = requests.post(url, auth=('***REMOVED***', ''), data=info, headers=headers)
   ret = json.loads(r.text)
   return ret
   
   
#Searches courses credits by its id
def tamk_credits(id):
   info = tamk_API_courseunits(id)
   credits = info['courseUnits'][0]['credits']
   return("Course "+str(id)+" is worth "+str(credits)+" credits.")
print(tamk_credits("IM00BR45"))