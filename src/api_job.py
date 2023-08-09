from abc import ABC, abstractmethod
import requests
import json
import time
import os



class APIJob(ABC):
    @abstractmethod
    def __init__(self, profession_name: str, cities: str, page: int = 0) -> None:
        self.profession_name = profession_name
        self.cities = cities
        self.page = page

    @abstractmethod
    def get(self):
        pass


class APIHeadHunter(APIJob):
    """ Класс для работы с конкретной платформой HeadHunter"""


    def __init__(self, profession_name: str, cities: str, page: int = 0) -> None:
        self.profession_name = profession_name
        self.cities = cities
        self.page = page

    def get(self):

        """
        Создаем метод для получения страницы со списком вакансий.
        Аргументы:
            page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
        """
        url = 'https://api.hh.ru/vacancies'

        # Справочник для параметров GET-запроса
        params = {
            'text': f'NAME:{self.profession_name}',  # Текст фильтра.
            'area': self.cities,  # Поиск осуществляется по вакансиям города
            'page': self.page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get(url, params)  # Посылаем запрос к API
        data = req.json()

        return data.get('items', [])


class APISuperJob(APIJob):
    """ Класс для работы с конкретной платформой SuperJob"""
    pass


class WorkingWithVacancies:
    """ Класс для работы с вакансиями"""
    def __init__(self, file_json):
        self.file_json = file_json
        for i in file_json:
            #print(i)
            try:
                self.name_vacancy = i['name']   # Название вакансии
                self.url_vacancy = i['url']   # Ссылка на вакансию
                self.salary_from_vacancy = i['salary']['from']   # Зарплата от
                self.salary_to_vacancy = i['salary']['to']   # Зарплата до
                self.requirement_vacancy = i['snippet']['requirement']   # Требования
                self.responsibility_vacancy = i['snippet']['responsibility']   # Обязанности
                self.experience_vacancy = i['experience']['name']   # Опыт

            except:
                self.salary_from_vacancy = None
                self.salary_to_vacancy = None


    def __repr__(self):
        return f'{self.name_vacancy}\n {self.url_vacancy}\n {self.salary_from_vacancy} - {self.salary_to_vacancy}\n {self.requirement_vacancy}\n {self.responsibility_vacancy}\n {self.experience_vacancy}'

    def compare_salary(self):


process = APIHeadHunter('Аналитик', 1, 0)
file = process.get()
#print(process.get())
name_vacancy = WorkingWithVacancies(file)
print(name_vacancy) # Печатаем Название вакансии
print(name_vacancy.experience_vacancy) # Печатаем Опыт
