from datetime import datetime
class Utils:
    """ Утилиты"""
    def __init__(self, data):
        self.data = data

    def len_vacancies(self):
        return len(self.data)

    def filter_vacancies(self, salary):
        result = []
        for i in self.data:
            if i['salary_to'] is not None:
                salary_int = i['salary_to']
                if salary_int > int(salary):
                    result.append(i)
        self.data = result

    def sorted(self, key=0):

        if key == '1':
            self.data = sorted(self.data, key=lambda x: datetime.strptime(x['date'], '%d %B %Y'), reverse=True)
            return self.data
        elif key == '2':
            self.data = sorted(self.data, key=lambda x: int(x['salary_to'] if x['salary_to'] else 0))
            return self.data
        elif key == '3':
            self.data = sorted(self.data, key=lambda x: int(x['salary_to']), reverse=True)
            return self.data
