import requests, json

def tamk_API_data():
   #TAMK 
   #URL and other info for API request
   url = 'https://opendata.tamk.fi/r1/courseunit/search'
   headers = {'Accept-Language':'en', 'content-type':'application/json'}
   info = {"codes": ["IM00BR45"]}
   info = json.dumps(info)
   loaded_info = json.loads(info)
   #Makes API-request and saves data into json-file.
   r = requests.post(url, auth=('***REMOVED***', ''), data=info, headers=headers)

   print(r)
   print(r.content)
  
   
   file = open("jsons/TAMK.json","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
tamk_API_data()