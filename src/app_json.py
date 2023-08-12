import json
from api_job import WorkingVacancies

class AppJson:

    def __init__(self, date):
        self.date = date


    def open_json(self):
        with open(f'vacancies_hh.txt', 'w', encoding='utf-8') as outfile:
            json.dump(self.date, outfile)





