class Vacancy:
    __slots__ = {"title", "link", "description", "salary"}

    def __init__(self, title, link, description, salary):
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (f"Vacancy(title='{self.title}', "
                f"link='{self.link}', "
                f"description='{self.description}', "
                f"salary='{self.salary}')")

    def __str__(self):
        return self.title

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        if other.salary is None:
            return False
        if self.salary is None:
            return True

        return self.salary < other.salary


class HHVacancy(Vacancy):
    def __str__(self):
        return f"HH: {self.title}, зарплата: {self.salary} руб/мес"


class SJVacancy(Vacancy):
    def __str__(self):
        return f"SJ: {self.title}, зарплата: {self.salary} руб/мес"
