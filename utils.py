"""
Модуль 2. Домашнее задание №10
Первое приложение на Flask. Знакомство с GIT.

Модуль с функциями.
"""

import json


def load_candidates():
    """
    Загружает базу данных по кандидатам из json файла
    и преобразует в словарь с доступом по id кандидата.
    :return: обработанная база данных кандидатов.
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates_data = json.load(file)
        candidates = {}
        for i in candidates_data:
            candidates[i['id']] = i
        return candidates


def available_skills_base(candidates_data):
    """
    Формирует базу навыков по всем предоставленным кандидатам.
    :param candidates_data: база данных кандидатов.
    :return: сортированное множество всей базы навыков.
    """
    skills_base = set()
    for candidate in candidates_data.values():
        # print(set(candidate["skills"].lower().split(', ')))
        skills_base.update(set(candidate["skills"].lower().split(', ')))

    return sorted(skills_base)
