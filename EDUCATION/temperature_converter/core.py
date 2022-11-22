"""
Полигон №2
"""

import os
import list_of_formula as lf

INFO_01 = '\nДля перемещения по программе используй цифры.\n' \
          'Целые цифры, не дробные, не выраженные словами.\n' \
          'Только цифры на клавиатуре.\n'

INFO_02 = 'Некая группа лис.\nОни прячутся в лесу, не отличаются ' \
          'сообразительностью...\nНо иногда у них что-то получается.'

INFO_03 = '\nСколько градусов?\n\n--Примечание--\nСуществует абсолютный ноль' \
          ' - минимальная возможная температура - 0K (-459.67°F, -273.15°C).' \
          '\nНиже этого значения температуры не существует.\nПо крайней ' \
          'мере, в нашей Вселенной.\n'

win_clear, lin_clear = 'cls', 'clear'


def cls():
    """Очистка консоли"""
    os.system(win_clear if os.name == 'nt' else lin_clear)


def main_menu():
    """Основное меню"""
    return ('\nКонвертер погоды v1.0\n'
            '\n--Основное меню--\n'
            '1. Информация.\n'
            '2. Конвертер.\n'
            '3. Выход.')


def information_menu():
    """Меню информации"""
    return ('\n--Меню информации--\n'
            '1. Как этим пользоваться.\n'
            '2. Кто тебя создал?\n'
            '3. Выход.')


def converter_menu():
    """Меню конвертера"""
    return ('\n--Меню конвертера--\n'
            '1. Цельсии.\n'
            '2. Кельвины.\n'
            '3. Фаренгейты.\n'
            '4. Выход.')


def converter_module():
    """Модуль конвертера"""
    cls()
    while True:
        print(converter_menu())
        convert_choice = int(input('\nЧто конвертируем?\n'))
        cls()
        if convert_choice == 4:
            cls()
            break
        temperature = float(input(INFO_03))
        if convert_choice == 1:  # Цельсий
            cls()
            print(f'Температура по Кельвину:'
                  f' {round(lf.celsius_in_kelvin(temperature), 2)}K')
            print(f'Температура по Фаренгейту:'
                  f' {round(lf.celsius_in_fahrenheit(temperature), 2)}°F')
        if convert_choice == 2:  # Кельвин
            cls()
            print(f'Температура по Цельсию:'
                  f' {round(lf.kelvin_in_celsius(temperature), 2)}°C')
            print(f'Температура по Фаренгейту:'
                  f' {round(lf.kelvin_in_fahrenheit(temperature), 2)}°F')
        if convert_choice == 3:  # Фаренгейт
            cls()
            print(f'Температура по Цельсию:'
                  f' {round(lf.fahrenheit_in_celsius(temperature), 2)}°C')
            print(f'Температура по Кельвину:'
                  f' {round(lf.fahrenheit_in_kelvin(temperature), 2)}K')


def info_module():
    """Модуль информации."""
    cls()
    while True:
        print(information_menu())
        sub_choice_01 = int(input('\nЧто-то конкретное?\n'))
        if sub_choice_01 == 1:
            cls()
            print(INFO_01)
        if sub_choice_01 == 2:
            cls()
            print(INFO_02)
        if sub_choice_01 == 3:
            cls()
            break


def start_module():
    """Модуль навигации"""
    while True:
        cls()
        print(main_menu())
        main_choice_01 = int(input('Приветствую! Что тебя интересует?\n'))
        if main_choice_01 == 1:
            info_module()
        if main_choice_01 == 2:
            converter_module()
        if main_choice_01 == 3:
            break


if __name__ == '__main__':
    start_module()
