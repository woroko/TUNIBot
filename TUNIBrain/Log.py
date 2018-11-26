import csv
from datetime import datetime

class Logger:
    def __init__(self, logs_on):
        self.logs_on = False
        if logs_on:
            self.logs_on = True
            currentDate = datetime.now()
            currentDate = currentDate.strftime('%H-%M-%S %d.%m.%Y')
            self.csvfile_s = open('Logs/Successful/'+ str(currentDate) +'.csv', 'w', newline='')
            self.csvfile_f = open('Logs/Failed/'+ str(currentDate) +'.csv', 'w', newline='')
            self.writer_s = csv.writer(self.csvfile_s, delimiter=',')
            self.writer_f = csv.writer(self.csvfile_f, delimiter=',')
            self.writer_s.writerow(['Question'] + ['Response'] + ['Intent_confidence'] + ['Intent_name'] + ['Top_entity_confidence'] + ['Top_entity_name'] + ['Source'])
            self.writer_f.writerow(['Question'] + ['Response'] + ['Intent_confidence'] + ['Intent_name'] + ['Top_entity_confidence'] + ['Top_entity_name'] + ['Source'])


    def log_success(self, Question, Response, Intent_confidence, Intent_name, Top_entity_confidence, Top_entity_name, Source):
        self.writer_s.writerow([Question] + [Response] + [Intent_confidence] + [Intent_name] + [Top_entity_confidence] + [Top_entity_name] + [Source])

    def log_failed(self, Question, Response, Intent_confidence, Intent_name, Top_entity_confidence, Top_entity_name, Source):
        self.writer_f.writerow([Question] + [Response] + [Intent_confidence] + [Intent_name] + [Top_entity_confidence] + [Top_entity_name] + [Source])


    def __del__(self):
        if self.logs_on:
            self.csvfile_s.close()
            self.csvfile_f.close()
