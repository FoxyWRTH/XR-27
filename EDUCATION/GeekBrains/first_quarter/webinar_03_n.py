"""
Домашняя работа. Лекция №3
"""

import random

# Task - 1/2
# Написать функцию num_translate(), переводящую числительные от 0 до 10
# C английского на русский язык.
# Например: >>> num_translate("one") "один" >>> num_translate("eight") "восемь"
# Если перевод сделать невозможно, вернуть None.

# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
# Результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") "Один"
# >>> num_translate_adv("two") "два"

def translate_adv(word):
    """Полностью законченная функция перевода, выполняет обе задачи"""
    word_dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if word[0].isupper():
        print(f'"{word_dictionary.get(word.lower()).title() if word.lower() in word_dictionary else None}"')
    else:
        print(f'"{word_dictionary.get(word.lower())}"')


translate_adv('Six')


# Task - 3/4
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

# Например:
# input: thesaurus("Иван", "Мария", "Петр", "Илья")
# output: { "И": ["Иван", "Илья"], "М": ["Мария"], "П": ["Петр"] }

# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий.
# Значения — словари, реализованные по схеме предыдущего задания.
# Содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Пётр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def dict_in_dict_stupid_system(*args):
    """То что я пока не смог сделать в улучшенном виде"""
    result_dict = {}
    for i in args:
        if i[0] not in result_dict:
            result_dict[i[0]] = []
        result_dict[i[0]].append(i)

    return result_dict


print(dict_in_dict_stupid_system("Иван", "Инна", "Пётр", "Илья", "Анна"))


# Task - 5
#
# Реализовать функцию get_jokes(), возвращающую n шуток
# Сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например: >>> get_jokes(2) ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг.
# Разрешающий или запрещающий повторы слов в шутках.
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?


def get_jokes(n_joke):
    """То что я пока не смог сделать в улучшенном виде"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    for _ in range(0, n_joke):
        random_jokes = f'{random.choice(nouns)}' \
                       f' {random.choice(adverbs)}' \
                       f' {random.choice(adjectives)}'
        result.append(random_jokes)
    return result


print(get_jokes(3))
