from src.class_api import HH, SJ
from src.class_file import File
from src.setting import HH_JSON, SJ_JSON
from src.utils import get_hh_vacancies_list, get_sj_vacancies_list, sorted_vacancy, top_vacancy


def main():
    print("Ищим вакансии:")
    do = ""
    while True:
        if do == "end":
            break
        else:
            name_vac = input("Vvedite nazvanie vacancii : ")
            hh_json = File(HH_JSON)
            hh_json.clean()
            sj_json = File(SJ_JSON)
            sj_json.clean()
            hh = HH(name_vac)
            sj = SJ(name_vac)
            hh_json.insert(hh.get_request().json()["items"])
            sj_json.insert(sj.get_request().json()["objects"])

            hh_get = get_hh_vacancies_list(hh_json)
            sj_get = get_sj_vacancies_list(sj_json)
            all_vac = hh_get + sj_get
            while True:
                do = input("Vvedite deystvie: vse, sort, top, new, end : ")
                if do == "vse":
                    for i in all_vac:
                        print(i)
                elif do == "sort":
                    sort_all_vac = sorted_vacancy(all_vac)
                    for i in sort_all_vac:
                        print(i)
                elif do == "top":
                    top_vac = top_vacancy(all_vac, top_count=10)
                    for i in top_vac:
                        print(i)
                elif do == "new":
                    break
                elif do == "end":
                    print("Poka")
                    break


if __name__ == '__main__':
    main()
