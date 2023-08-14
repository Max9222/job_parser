from src.api_job import ApiHH, ApiSuperJob
from src.utils import Utils

from src.app_json import AppJson

if __name__ == '__main__':
    print()
    print("Привет мой друг, данный программный модуль поможет тебе с поиском работы.")
    print()
    print("Для начала определись с вакансией")
    keyword = input("Какой твой выбор?\n: ")

    print()
    # Для HH
    hh = ApiHH(keyword)
    vac_hh = hh.get_vacancies()
    list_hh = hh.get_formatted(vac_hh)   # подгоняем под удобрый формат
    #print(list_hh)

    # Для SJ
    sj = ApiSuperJob(keyword)
    vac_sj = sj.get_vacancies()
    list_sj = sj.get_formatted(vac_sj)   # подгоняем под удобрый формат

    # Экземпляр для записи в файл
    list_1 = list_hh + list_sj
    app_json = AppJson(keyword, list_1)
    write_json = app_json.write_json()  # Записали
    read_json = app_json.read_json()    # Прочитали
    #print(read_json)

    # Утилиты
    utils = Utils(read_json)
    len_list_1 = utils.len_vacancies()  # Считаем кол-во запросса в файле Python.json

    yes_no = input("""Хочешь узнать сколько мы нашли вакансий?
    yes - Конечно хочу =)
    no - Нет мне не интересно!!!
    : """)

    if yes_no.lower() == 'yes':
        if vac_hh:
            print(f"По запросу найдено {len_list_1} вакансий")
        else:
            print("Ничего не найдено")
    else:
        pass
    print()
    # Фильтр по ЗП

    print("Следующий шаг ---")
    salary = input("Какой минимальный порог по ЗП?\n: ")

    # Сортируем
    min_salary = utils.filter_vacancies(salary)
    len_list_2 = utils.len_vacancies()
    # print(min_salary)
    print(f"По запросу найдено {len_list_2} вакансий")
    print()

    print("По умолчанию сортировка по дате")
    sorted = input("""Можно выбрать сортировку 
    1 - по дате (реверсивную)
    2 - Сортировка по ЗП от Мах -> Мин
    3 - Сортировка по ЗП от Мин -> Мах
    : """)
    utils_1 = Utils(read_json) # Читаем файл

    sort = utils_1.sorted(sorted)
    app2 = AppJson(keyword, sort)   # Сортируем
    write = app2.write_json()   # Записываем
    print()

    print("Вакансии отсортированы в соответствии с вашим запросом")
    print(f"Данными можно воспользоваться, они в этом файле --> {keyword}.json")


