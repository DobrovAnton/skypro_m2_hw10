from flask import Flask
import utils

app = Flask(__name__)

candidates = utils.load_candidates()
skills_base = utils.available_skills_base(candidates)


@app.route("/")
def page_candidate_list():
    candidates_str = "<pre>\n"

    for candidate in candidates.values():
        candidates_str += f"{candidate['name']}\n" \
                          f"{candidate['position']}\n" \
                          f"{candidate['skills']} \n\n"
    candidates_str += "<pre>"

    return candidates_str


@app.route("/candidate/<int:id_>")
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


@app.route("/skills/<skills>")
def page_skills(skills):
    candidate_str = "<pre>\n"

    if skills not in skills_base:
        return 'Кандидатов с указанным навыком не обнаружено.'

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


if __name__ == "__main__":
    app.run(debug=True)
