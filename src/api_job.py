from abc import ABC, abstractmethod
import requests
import json
import time
import os


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
                'salary_from': i['salary']['from'] if i['salary'] else None,  # Зарплата от
                'salary_to': i['salary']['to'] if i['salary'] else None,  # Зарплата до
                'requirement': i['snippet']['requirement'],  # Требования
                'responsibility': i['snippet']['responsibility'],  # Обязанности
                'experience': i['experience']['name'],  # Опыт
            }
            self.vacancies.append(dict_aa)
        return self.vacancies


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
##########

class Vacancy:
    """ Класс для работы с вакансиями"""
    def __init__(self, data: list):
        self.data = data


    def list_json(self):
        lis = []
        for i in self.data:
            #print(i)

            dict_aa = {
                'id': i['id'],   # id вакансии
                'name': i['name'],   # Название вакансии
                'url': i['url'],   # Ссылка на вакансию
                'salary_from': i['salary']['from'] if i['salary'] else None,   # Зарплата от
                'salary_to': i['salary']['to'] if i['salary'] else None,   # Зарплата до
                'requirement': i['snippet']['requirement'],   # Требования
                'responsibility': i['snippet']['responsibility'],   # Обязанности
                'experience': i['experience']['name'],   # Опыт
            }
            lis.append(dict_aa)
        return lis

##########

class Vacancyinit:
    def __init__(self, vacancy):
        for i in vacancy:
            self.id = i['id'],  # id вакансии
            self.name = i['name'],  # Название вакансии
            self.url = i['url'],  # Ссылка на вакансию
            self.salary_from = i['salary']['from'] if i['salary'] else None,  # Зарплата от
            self.salary_to = i['salary']['to'] if i['salary'] else None,  # Зарплата до
            self.req = i['snippet']['requirement'],  # Требования
            self.resp = i['snippet']['responsibility'],  # Обязанности
            self.exp = i['experience']['name'],  # Опыт
            #self.currency = i['currency'] if None else None
            #self.currency_value = i['currency_value']
            self.employer = i['employer']
            #self.title = i['title']

    def __str__(self):
        if not self.salary_from and not self.salary_to:
            salary = " Отсутствует"
        else:
            salary_from, salary_to = "", ""
            if self.salary_from:
                salary_from = f"от { self.salary_from} {self.currency}"
                if self.currency != "RUR":
                    salary_from += f"({ round(self.salary_from * self.currency_value, 2) } RUR"
            if self.salary_to:
                salary_to = f"до { self.salary_to } { self.currency }"
                if self.currency != "RUR":
                    salary_to += f" ({ round(self.salary_to * self.currency_value, 2)} RUR"
            salary = " ".join([salary_from, salary_to]).strip()
        return f"""
Работодатель: \"{ self.employer }\"
Вакансия: \"{ self.title }\"
Зарплата: { salary }
Ссылка: { self.url }
        """
##########

class AppJson:

    def __init__(self, keyword, date):
        self.filename = f'{ keyword.title() }.json'
        self.date = date

    def write_json(self):
        with open(self.filename, 'w', encoding='utf-8') as outfile:
            json.dump(self.date, outfile, indent=4)


    def read_json(self):
        with open(self.filename, 'r', encoding="utf-8") as infile:
            vacancies = json.load(infile)
        return [Vacancy(x) for x in vacancies]


class Utils:
    """ Утилиты"""
    def __init__(self, data):
        self.data = data

    def len_vacancy(self):
        return len(self.data)

    def filter_vacancies(self, key_filter):
        result = []
        for i in self.data:
            if i['salary_top'] == None:
                if i['salary_low'] == None:
                    i['salary_top'] = 0
                else:
                    i['salary_top'] = i['salary_low']
            if i['salary_top'] >= int(key_filter):
                result.append(i)
        self.data = result