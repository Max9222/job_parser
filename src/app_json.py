import json

class AppJson:
    """ Класс для работы с Json"""

    def __init__(self, keyword, date):
        self.filename = f'{ keyword.title() }.json'
        self.date = date

    def write_json(self):
        with open(self.filename, 'w', encoding='utf-8') as outfile:
            json.dump(self.date, outfile, indent=4)


    def read_json(self):
        with open(self.filename, 'r', encoding="utf-8") as infile:
            vacancies = json.load(infile)
        return vacancies





