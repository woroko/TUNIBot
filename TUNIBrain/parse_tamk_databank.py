import requests, json

def get_data():
    try:
        #URL and other info for API request
        url = 'https://opendata.tamk.fi/r1/realization/search'
        headers = {'Accept-Language':'en', 'content-type':'application/json'}
        info = { "startDate": "2015-01-01T00:00:00"}
        info = json.dumps(info)
        loaded_info = json.loads(info)

        #Makes API-request and saves the data in json-form.
        r = requests.post(url, auth=('***REMOVED***', ''), data=info, headers=headers)
        ret = json.loads(r.text)
        file = open("jsons/tamk_course_implementations.json","w") 
        file.write(r.content.decode('utf-8'))
        file.close()
    except Exception as e:
        print(e)
    return None

class TAMKJsonParser:
    def parse_files(self):
        with open('jsons/tamk_course_implementations.json', 'r') as f:
            self.course_implementations = json.load(f)
            
    def __init__(self):
        self.parse_files()
        
#Takes all course codes from API and dumps them into text file        
def dump_course_codes(parser):
    with open("tamk_course_codes.txt", 'w') as f:
        for course in parser.course_implementations['realizations']:
            code = course['code']
            if len(code) > 1:
                f.write(code + "\n")

#Takes all course names from API and dumps them into text file
def dump_course_names(parser):
    with open("tamk_course_names.txt", 'w') as f:
        for course in parser.course_implementations['realizations']:
            name = course['name']
            if len(name) > 1:
                f.write(name + "\n")

                
def main():
    parser = TAMKJsonParser()
    print(len(parser.course_implementations))
    print(parser.course_implementations['realizations'][0]['code'])

    
if __name__ == "__main__":
    main()