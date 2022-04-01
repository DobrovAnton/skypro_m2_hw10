"""
Модуль 2. Домашнее задание №10
Первое приложение на Flask. Знакомство с GIT.

Создание приложение на Flask;
Роуты без параметров;
Роуты с параметрами.

"""

# Импорт Flask и функций.
from flask import Flask
import utils

app = Flask(__name__)

# Загрузка данных кандидатов из json файла.
candidates = utils.load_candidates()

# Список всех возможных навыков.
skills_base = utils.available_skills_base(candidates)


# Основная страница всех кандидатов из базы.
# Роут без параметра.
@app.route("/")
def page_candidate_list():
    candidates_str = "<pre>\n"

    for candidate in candidates.values():
        candidates_str += f"{candidate['name']}\n" \
                          f"{candidate['position']}\n" \
                          f"{candidate['skills']} \n\n"
    candidates_str += "<pre>"

    return candidates_str


# Станица кандидата по id. Роут с параметром.
@app.route("/candidate/<int:id_>/")
def page_profile(id_):

    if id_ not in candidates.keys():
        return f'Кандидат с ID {id_} отсутствует.'

    else:
        candidate = candidates[id_]
        candidate_str = f"<img src={candidate['picture']}></img>\n\n"\
                        f"<pre>\n" \
                        f"{candidate['name']}\n"\
                        f"{candidate['position']}\n"\
                        f"{candidate['skills']}<pre> \n\n"

        return candidate_str


# Страница кандидатов с запрашиваемым навыком. Роут с параметром.
@app.route("/skills/<skills>/")
def page_skills(skills):
    candidate_str = "<pre>\n"

    # Условие если нет кандидатов с запрашиваемым навыком.
    if skills not in skills_base:
        return 'Кандидатов с указанным навыком не найдено.'

    # Условие отображение кандидатов с запрашиваемым навыком.
    else:
        for candidate in candidates.values():
            candidate_skills = candidate["skills"].lower().split(', ')
            if skills in candidate_skills:
                candidate_str += f"{candidate['name']}\n" \
                                 f"{candidate['position']}\n" \
                                 f"{candidate['skills']}\n" \
                                 f"\n"
        candidate_str += "<pre>"

        return candidate_str


# Запуск веб-приложения.
if __name__ == "__main__":
    app.run(debug=True)
