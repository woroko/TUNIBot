import csv
from datetime import datetime

def successful_log(Question, Response, Intent_confidence, Intent_name, Top_entity_confidence, Top_entity_name, Source):
    currentDate = datetime.now()
    currentDate = currentDate.strftime(' %H-%M-%S %d.%m.%Y')
    with open('Logs/Successful/Successful'+ str(currentDate) +'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Question'] + ['Response'] + ['Intent_confidence'] + ['Intent_name'] + ['Top_entity_confidence'] + ['Top_entity_name'] + ['Source'])
        writer.writerow([Question] + [Response] + [Intent_confidence] + [Intent_name] + [Top_entity_confidence] + [Top_entity_name] + [Source])
    
def failed_log(Question, Response, Intent_confidence, Intent_name, Top_entity_confidence, Top_entity_name, Source):
    currentDate = datetime.now()
    currentDate = currentDate.strftime(' %H-%M-%S %d.%m.%Y')
    with open('Logs/Failed/Failed'+ str(currentDate) +'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Question'] + ['Response'] + ['Intent_confidence'] + ['Intent_name'] + ['Top_entity_confidence'] + ['Top_entity_name'] + ['Source'])
        writer.writerow([Question] + [Response] + [Intent_confidence] + [Intent_name] + [Top_entity_confidence] + [Top_entity_name] + [Source])
