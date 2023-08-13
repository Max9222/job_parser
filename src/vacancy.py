class Vacancy:
    def __init__(self, vacancy):
        for i in vacancy:
            self.id = i['id'],  # id вакансии
            self.name = i['name'],  # Название вакансии
            self.url = i['url'],  # Ссылка на вакансию
            self.salary_from = i['salary']['from'] if i['salary'] else 0,  # Зарплата от
            self.salary_to = i['salary']['to'] if i['salary'] else 0,  # Зарплата до
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
#############