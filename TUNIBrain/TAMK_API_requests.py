import requests, json

def tamk_API_data():
   #TAMK 
   #URL and other info for API request
   url = 'https://opendata.tamk.fi/r1/courseunit/search'
   headers = {'Accept-Language':'en'}
   info = {"codes": ["18YTIKO"]}
   info = json.dumps(info)
   loaded_info = json.loads(info)
   #Makes API-request and saves data into json-file.
   r = requests.get(url, auth=('***REMOVED***', ''), data=loaded_info, headers=headers)
   j=json.loads(r.text)
   print(j)
   
   file = open("jsons/TAMK.json","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
tamk_API_data()