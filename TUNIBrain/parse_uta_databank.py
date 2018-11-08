import json
#from dateutil import datetime
from datetime import datetime
import dateutil.parser
import traceback

import math

class UTAJsonParser:
    def parse_files(self, json_dir):
        with open(json_dir + '/uta_course_implementations.json', 'r', encoding="latin-1") as f:
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
        matches = self.search_regular_course_implementation(id=id)
        ordered_matches = []
        currentDate = datetime.now()
        for i in range(0, len(matches)):
            try:
                start = dateutil.parser.parse(matches[i]['startDate'])
                diff = start - currentDate
                ordered_matches.append((i, math.fabs(diff.total_seconds())))
            except Exception as e:
                print(e)
                print("find_course_start_date invalid")

        response = ""
        if len(matches) > 0:
            try:
                '''response += "Found matching courses at UTA."
                if len(matches) > 1:
                    response += " Displaying top 3."
                response += "\n"'''
                i=0
                for match in sorted(ordered_matches, key=lambda x: x[1]):
                    if i > 2:
                        break
                    course_json = matches[match[0]]
                    if match[1] < 63113851.0: # 2 years
                        response += "  Course " + course_json['name'] + " starts " \
                            + course_json['startDate'] + ".\n"
                    i += 1
            except Exception as e:
                print("find_course_start_date error")

        return response

    def find_course_teachinglanguage(self, id):
        matches = self.search_regular_course_implementation(id=id)
        ordered_matches = []
        currentDate = datetime.now()
        for i in range(0, len(matches)):
            try:
                start = dateutil.parser.parse(matches[i]['startDate'])
                diff = start - currentDate
                ordered_matches.append((i, math.fabs(diff.total_seconds())))
            except Exception as e:
                print(e)
                print("find_course_teachinglanguage invalid")

        response = ""

        try:
            #response += "Found matching courses at UTA:\n"
            match = sorted(ordered_matches, key=lambda x: x[1])[0]
            course_json = matches[match[0]]
            if match[1] < 63113851.0:
                lang = ""
                if course_json['teachingLanguage'] == "sv":
                    lang = "Swedish"
                elif course_json['teachingLanguage'] == "fi":
                    lang = "Finnish"
                elif course_json['teachingLanguage'] == "en":
                    lang = "English"

                response += "  Course " + course_json['name'] + " teaching language is " \
                + lang + ".\n"

        except Exception as e:
            traceback.print_exc()
            print("find_course_teachinglanguage error")

        return response

    def find_course_teaching_times(self, id):
        matches = self.search_regular_course_implementation(id=id)
        ordered_matches = []
        currentDate = datetime.now()
        for i in range(0, len(matches)):
            try:
                start = dateutil.parser.parse(matches[i]['startDate'])
                diff = start - currentDate
                ordered_matches.append((i, math.fabs(diff.total_seconds())))
            except Exception as e:
                print(e)
                print("find_course_teaching_times invalid")

        response = ""
        if len(matches) > 0:
            try:
                #response += "Found matching courses at UTA.\n"
                '''if len(matches) > 1:
                    response += " Displaying top 3."'''
                #response += "\n"
                i=0
                for match in sorted(ordered_matches, key=lambda x: x[1]):
                    if i > 2:
                        break
                    course_json = matches[match[0]]
                    if match[1] < 63113851.0: # 2 years
                        response += "  Course " + course_json['name'] + ", start date " \
                            + course_json['startDate'] + ".\n"
                        #response += "Study groups and schedules: \n"
                        group_idx = 0
                        for group in course_json['_opsi_opryhmat']:
                            if (group['nimi'] is not None):
                                response += "  " + group['nimi'] + "\n"
                            else:
                                response += "    Group " + str(group_idx) + "\n"
                            for time in group['ajat']:
                                #print(time['alkuaika'])
                                starttime = datetime.utcfromtimestamp(time['alkuaika']//1000).strftime('%d-%m-%Y')
                                if time['toistuvuus'] is not None:
                                    endtime = datetime.utcfromtimestamp(time['alkuaika']//1000).strftime('%d-%m-%Y')
                                    alkuminuutit = time['alkuminuutit']
                                    if len(alkuminuutit) < 1:
                                        alkuminuutit = "00"
                                    loppuminuutit = time['loppuminuutit']
                                    if len(loppuminuutit) < 1:
                                        loppuminuutit = "00"
                                    response += "      From " + starttime + " to " \
                                        + endtime + ", " + time['alkutunnit'] + ":" \
                                        + alkuminuutit + "-" + time['lopputunnit'] \
                                        + ":" + loppuminuutit + ", in " + time['paikka'] + "\n"
                                else:
                                    alkuminuutit = time['alkuminuutit']
                                    if len(alkuminuutit) < 1:
                                        alkuminuutit = "00"
                                    loppuminuutit = time['loppuminuutit']
                                    if len(loppuminuutit) < 1:
                                        loppuminuutit = "00"
                                    response += "      " + starttime + ", " + time['alkutunnit'] + ":" \
                                    + alkuminuutit + "-" + time['lopputunnit'] \
                                    + ":" + loppuminuutit + ", in " + time['paikka'] + "\n"

                    i += 1
            except Exception as e:
                traceback.print_exc()
                print("find_course_teaching_times error")

        return response



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
    #print(parser.course_implementations[0]['name'])
    print(len(parser.course_implementations))
    print(parser.find_course_start_date("KKSULUK"))
    print(parser.find_course_teaching_times("KKSULUK"))
    print(parser.find_course_teachinglanguage("KKSULUK"))


if __name__ == "__main__":
    main()
