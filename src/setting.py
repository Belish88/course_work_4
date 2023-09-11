from pathlib import Path

HH_URL = "https://api.hh.ru/vacancies"
SJ_URL = "https://api.superjob.ru/2.0/vacancies/"
ROOT = Path(__file__).resolve().parent.parent
SRC = Path.joinpath(ROOT, "src")
HH_JSON = Path.joinpath(SRC, "hh.json")
SJ_JSON = Path.joinpath(SRC, "sj.json")
