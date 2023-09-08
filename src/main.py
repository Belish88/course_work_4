from src.class_api import HH, SJ
from src.class_file import File
from src.class_vacancy import HHVacancy
from src.utils import get_hh_vacancies_list, get_sj_vacancies_list


def main():
    file = File("data.json")
    hh = HH("python")
    # sj = SJ("python")
    #
    file.insert(hh.get_request().json()["items"])
    # file.insert(sj.get_request().json()["objects"])

    s = get_hh_vacancies_list(file)
    for i in s:
        print(i)
    # print(get_sj_vacancies_list(file))

if __name__ == '__main__':
    main()
