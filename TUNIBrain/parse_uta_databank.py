import json

class UTAJsonParser:
    def __init__(self, json_dir):
        with open(json_dir + '/uta_toteutukset.json', 'r') as f:
            self.toteutukset = json.load(f)

    '''def search_regular_course_implementation(id=None, name=None):
        if id is not None:
            for toteutus in self.toteutukset:
                if toteutus['']'''


def main():
    parser = UTAJsonParser("jsons")
    print(parser.toteutukset[0]['name'])
    print(len(parser.toteutukset))
    with open("course_codes.txt", 'w') as f:
        for course in parser.toteutukset:
            code = course['code']
            if len(code) > 1:
                f.write(code + "\n")


if __name__ == "__main__":
    main()
