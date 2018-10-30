import requests, time

#Loads University API-data and saves it into json and xml files.
def save_API_data():

   #Is there a delay between API calls or not
   delay = False
   
   #Implementation of study modules
   #URL and API-key for the request
   url = 'https://opendata.uta.fi:8443/apiman-gateway/UTA/opintojaksot/1.0'
   headers = {'X-API-Key':'***REMOVED***', 'content-type': 'application/json'}
   #Makes API-request and saves data into json-file.
   r = requests.post(url, data="{}", headers=headers)
   file = open("jsons/uta_course_implementations.json","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
   if(delay):
      time.sleep(30)
      
   #Open university studies
   #URL and API-key for the request
   url = 'https://opendata.uta.fi:8443/apiman-gateway/UTA/tarjontaavoin/1.0'
   headers = {'X-API-Key':'***REMOVED***', 'content-type': 'application/json'}
   #Makes API-request and saves data into xml-file.   
   r = requests.post(url, data="{}", headers=headers)
   file = open("xmls/available_studies_at_open_university.xml","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
   if(delay):
      time.sleep(30)
   
   #Exchange information
   #URL and API-key for the request
   url = 'https://opendata.uta.fi:8443/apiman-gateway/UTA/kvkohteet/1.0'
   headers = {'X-API-Key':'***REMOVED***', 'content-type': 'application/json'}
   #Makes API-request and saves data into json-file.
   r = requests.post(url, data="{}", headers=headers)
   file = open("jsons/exchange_destinations_and_programs.json","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
   
   if(delay):
      time.sleep(30)

   #Cross-institutional studies
   #URL and API-key for the request
   url = 'https://opendata.uta.fi:8443/apiman-gateway/UTA/tarjontat3/1.0'
   headers = {'X-API-Key':'***REMOVED***', 'content-type': 'application/json'}
   #Makes API-request and saves data into xml-file.
   r = requests.post(url, data="{}", headers=headers)
   file = open("xmls/cross-institutional_studies.xml","w") 
   file.write(r.content.decode('utf-8'))
   file.close()
   
save_API_data()