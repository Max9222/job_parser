from src.api_job import ApiHH
from src.utils import Utils
from src.vacancy import Vacancy
from src.app_json import AppJson

if __name__ == '__main__':
    vac_json = []
    #keyword = input("Какая вакансия?\n")
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
    #print(read_json)

    # Утилиты
    utils = Utils(read_json)
    len_list_1 = utils.len_vacancies()  # Считаем кол-во запросса в файле Python.json

    if vac_hh:
        print(f"По запросу найдено {len_list_1} вакансий")
    else:
        print("Ничего не найдено")

    # Фильтр по ЗП
    #salary = input("Какой минимальный порог по ЗП?\n")
    salary = 60000

    min_salary = utils.filter_vacancies(salary)  # Сортируем
    len_list_2 = utils.len_vacancies()
    #print(min_salary)
    print(f"По запросу найдено {len_list_2} вакансий")


    print("По умолчанию сортировка по дате")
    sorted = input("""Можно выбрать сортировку 
    1 - по дате (реверсивную)
    2 - Сортировка по ЗП от Мах -> Мин
    3 - Сортировка по ЗП от Мин -> Мах
    """)
    utils_1 = Utils(read_json) #Читаем файл
    #print(utils_1.data)
    sort = utils_1.sorted(sorted)
    app2 = AppJson(keyword, sort)   # Сортируем
    write = app2.write_json()   # Записываем


    print("Вакансии отсортированы в соответствии с вашим запросом")
    print("Данные в фале Python.json")
