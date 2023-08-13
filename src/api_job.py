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

        req = requests.get(self.url, self.params)  # Посылаем запрос к API
        #if req.status_code !=200:
        #    raise ParsingError(f"Ошибка получения вакансий! Статус: {req.status_code}")
        data = req.json()

        return data.get('items', [])

    def get_formatted(self, data):
        pass
        #print(data)
        for i in data:
            # print(i)

            dict_aa = {
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
            self.vacancies.append(dict_aa)
        return self.vacancies

#############

class ApiSuperJob(APIJob):
    """ Класс для работы с конкретной платформой SuperJob"""
    url = "https://api.superjob.ru/2.0/vacancies/"
    def __init__(self, keyword):
        self.params = {
            "count": 100,
            "page": None,
            "keyword": keyword,
            "archive": False
        }
        self.headers = {
            "X-Api-App-Id": ""
        }
        self.vacancies = []


    def get_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        return response.json()["objects"]
    pass

    def get_formatted(self):
        formatted_vacancies = []
        currencies = get_currencies()
        sj_currencies = {
            "rub": "RUB",
            "uah": "UAH",
            "uzs": "UZS",
        }

        for vacancy in self.vacancies:
            formatted_vacancy = {
                "employer": vacancy["firm_name"],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "api": "SuperJob",

            }
            #if :


            #else:
            #    formatted_vacancy["currency"] = None
            #    formatted_vacancy["currency_value"] = None

            #formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies

#############




#############


#############




#############




