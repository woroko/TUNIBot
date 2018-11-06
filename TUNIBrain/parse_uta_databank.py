import json
import dateutil
import math

class UTAJsonParser:
    def parse_files(self, json_dir):
        with open(json_dir + '/uta_course_implementations.json', 'r') as f:
            self.course_implementations = json.load(f)

    def __init__(self, json_dir):
        self.parse_files(json_dir)

    def search_regular_course_implementation(self, id=None, name=None):
        courses = []
        try:
            if id is not None:
                for course in self.course_implementations:
                    if id.lower() == course['code'].lower():
                        courses.append(course)
            if name is not None:
                for course in self.course_implementations:
                    if name.lower() in course['name'].lower():
                        courses.append(course)
        except Exception as e:
            print(e)

        return courses

    def current_date_sort(date):
        pass

    def find_course_start_date(self, id):
        matches = search_regular_course_implementation(id=id)
        ordered_matches = []
        currentDate = dateutil.datetime.now()
        for i in range(0, len(matches)):
            try:
                start = dateutil.parser.parse(matches[i]['startDate'])
                diff = date - currentDate
                ordered_matches.append((i, math.abs(diff.total_seconds())))
            except Exception:
                print("find_course_start_date invalid")

        response = ""
        if len(matches > 0):
            response += "Found " + str(len(matches)) +" matching course(s) at UTA."
            if len(matches) > 1:
                response += " Displaying top 3."
            response += "\n"
            i=0
            for match in sorted(ordered_matches, key=lambda x: x[1]):
                if i > 2:
                    break
                course_json = matches[match[0]]
                response += "Course " + course_json['name'] + " starts " \
                    + course_json['startDate']
                i += 1

    def search_tampub(self, id=None, name=None):
        pubs = []
        try:
            pass
        except Exception as e:
            print(e)

        return courses

def dump_course_codes(parser):
    with open("course_codes.txt", 'w') as f:
        for course in parser.course_implementations:
            code = course['code']
            if len(code) > 1:
                f.write(code + "\n")

def main():
    parser = UTAJsonParser("jsons")
    print(parser.course_implementations[0]['name'])
    print(len(parser.course_implementations))
    print(parser.search_regular_course_implementation(name='Filosofian historia'))



if __name__ == "__main__":
    main()
