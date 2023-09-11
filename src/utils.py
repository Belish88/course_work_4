from src.class_vacancy import HHVacancy, SJVacancy


def get_hh_vacancies_list(connector) -> list[HHVacancy]:
    vacancies = [
        HHVacancy(
            title=vacancy["name"],
            link=vacancy["alternate_url"],
            description=vacancy["snippet"],
            salary=vacancy["salary"]["from"] if vacancy["salary"] else None)
        for vacancy in connector.select({})]
    return vacancies


def get_sj_vacancies_list(connector):
    vacancies = [
        SJVacancy(
            title=vacancy["profession"],
            link=vacancy["link"],
            description=vacancy["candidat"],
            salary=vacancy["payment_from"])
        for vacancy in connector.select({})]
    return vacancies


def sorted_vacancy(vacancy):
    return sorted(vacancy)


def top_vacancy(vacancy, top_count):
    return list(sorted(vacancy, reverse=True)[:top_count])
