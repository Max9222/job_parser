import requests
import json
from src.api_job import ApiHH, AppJson, Vacancyinit, Utils


vac_json = []
#keyword = input(" Какая вакансия?")
keyword = "Python"


# Для HH
hh = ApiHH(keyword)
vac_hh = hh.get_vacancies()
list_hh = hh.get_formatted(vac_hh)
#print(list_hh)

# Экземпляр для записи в файл
list_1 = list_hh # + SuperJob
app_json = AppJson(keyword, list_1)
write_json = app_json.write_json()  # Записали
read_json = app_json.read_json()    # Прочитали

# Утилиты
utils = Utils(read_json)
len_list_1 = utils.len_vacancy()  # Считаем кол-во запросса в файле Python.json

if vac_hh:
    print(f"По запросу найдено {len_list_1} вакансий")
else:
    print("Ничего не найдено")

#Фильтр по ЗП








#keyword = 'Аналитик'
# Класс ApiHH
#api = ApiHH(keyword)
#data = api.get_vacancies()
#print(data)
# Отработала

# Класс Vacancy
#vacancy = Vacancy(data)
#list1 = vacancy.list_json()
#print(list1)
# Отработал

# Класс AppJson
#app = AppJson(keyword, list1)
#app_file = app.open_json()
#load_file = app.read()
#print(load_file)
# Отработал

# Класс Vacancyinit
#vac_init = Vacancyinit(data)
#print1 = vac_init.employer
#print(print1)

# Отработал


