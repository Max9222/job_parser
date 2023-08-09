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

        # Справочник для параметров GET-запроса
        params = {
            'text': f'NAME:{self.profession_name}',  # Текст фильтра.
            'area': self.cities,  # Поиск осуществляется по вакансиям города
            'page': self.page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.json()

        return data


class APISuperJob(APIJob):
    pass


process = APIHeadHunter('Аналитик', 1, 0)
process.get()
print(process.get())