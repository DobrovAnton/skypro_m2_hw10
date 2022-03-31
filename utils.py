import json
from pprint import pprint


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates_data = json.load(file)
        candidates = {}
        for i in candidates_data:
            candidates[i['id']] = i
        return candidates


def available_skills_base(candidates_data):
    skills_base = set()
    for candidate in candidates_data.values():
        # print(set(candidate["skills"].lower().split(', ')))
        skills_base.update(set(candidate["skills"].lower().split(', ')))

    return sorted(skills_base)



