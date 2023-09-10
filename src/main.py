from src.class_api import HH, SJ
from src.class_file import File
from src.class_vacancy import HHVacancy
from src.setting import HH_JSON, SJ_JSON
from src.utils import get_hh_vacancies_list, get_sj_vacancies_list


def main():
    hh_json = File(HH_JSON)
    sj_json = File(SJ_JSON)
    hh = HH("косметолог")
    sj = SJ("косметолог")

    hh_json.insert(hh.get_request().json()["items"])
    sj_json.insert(sj.get_request().json()["objects"])

    hh_get = get_hh_vacancies_list(hh_json)
    sj_get = get_sj_vacancies_list(sj_json)
    all_vac = hh_get + sj_get
    for i in all_vac:
        print(i)

    # hh_sel = hh_json.select(60000)
    # print(hh_sel)
    # for i in sel:
    #     print(i)

if __name__ == '__main__':
    main()
