class Vacancy:
    def __init__(self, vacancy):
        for i in vacancy:
            self.id = i['id'],  # id вакансии
            self.name = i['name'],  # Название вакансии
            self.url = i['url'],  # Ссылка на вакансию
            self.salary_from = i['salary_from'] if i['salary_from'] else 0,  # Зарплата от
            self.salary_to = i['salary_to'] if i['salary_to'] else 0,  # Зарплата до



    def __str__(self):

        return f"""
Название вакансии: { self.name}
Работодатель{self.employer}
Вакансия:{self.id}
Ссылка: {self.url}
        """
