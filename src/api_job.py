from abc import ABC, abstractmethod
import requests
from datetime import datetime




class APIJob(ABC):

    @abstractmethod
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword


    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_formatted(self):
        pass

#############


class ApiHH(APIJob):
    """ Класс для работы с конкретной платформой HeadHunter"""
    url = 'https://api.hh.ru/vacancies'
    def __init__(self, keyword):
        self.keyword = keyword

        self.params = { # Справочник для параметров GET-запроса
            'text': f'NAME:{self.keyword}',  # Текст фильтра.
            'area': 1,  # Поиск осуществляется по вакансиям города
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        self.vacancies = []


    def get_vacancies(self):
        """ Метод выполняющий запрос"""

        req = requests.get(self.url, self.params)  # Посылаем запрос к API
        #if req.status_code !=200:
        #    raise ParsingError(f"Ошибка получения вакансий! Статус: {req.status_code}")
        data = req.json()

        return data.get('items', [])

    def get_formatted(self, data):
        """ Получение стандартного списка"""

        #print(data)
        for i in data:
            # print(i)

            dict_hh = {
                'id': i['id'],  # id вакансии
                'name': i['name'],  # Название вакансии
                'url': i['url'],  # Ссылка на вакансию
                'salary_from': i['salary']['from'] if i['salary'] else 0,  # Зарплата от
                'salary_to': i['salary']['to'] if i['salary'] else 0,  # Зарплата до
                'requirement': i['snippet']['requirement'],  # Требования
                'responsibility': i['snippet']['responsibility'],  # Обязанности
                'experience': i['experience']['name'],  # Опыт
                'date': datetime.strptime(i['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d %B %Y'),
            }
            self.vacancies.append(dict_hh)
        return self.vacancies

#############




class ApiSuperJob(APIJob):
    """ Класс для работы с конкретной платформой SuperJob"""

    url = "https://api.superjob.ru/2.0/vacancies/"
    secret_key = "v3.r.117089974.d71ab5a2bdd1d45fafb10374b3a99703e7f54290.8916a32e83738bcbe6ed05697beffc1251f75ea8"
    id = '2867'


    def __init__(self, keyword):
        self.keyword = keyword

        self.params = {
            "count": 100,
            "page": 0,
            "keyword": self.keyword,
            "archive": False,
            'payment_from': 0,
        }

        self.vacancies = []


    def get_vacancies(self):
        """ Метод выполняющий запрос"""

        response = requests.get(self.url, headers={"X-Api-App-Id": self.secret_key}, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        return response.json()["objects"]


    def get_formatted(self, data):
        """ Получение стандартного списка"""
        for i in data:
            dict_sj = {
                'id': i['id'],  # id вакансии
                'name': i['profession'],  # Название вакансии
                'url': i['link'],  # Ссылка на вакансию
                'salary_from': i['payment_from'] if i['payment_from'] else 0,  # Зарплата от
                'salary_to': i['payment_to'] if i['payment_to'] else 0,  # Зарплата до
                #'requirement': i['snippet']['requirement'],  # Требования
                #'responsibility': i['snippet']['responsibility'],  # Обязанности
                #'experience': i['experience']['name'],  # Опыт
                'date': datetime.fromtimestamp(i['date_published']).strftime('%d %B %Y'),
            }
            self.vacancies.append(dict_sj)
        return self.vacancies


