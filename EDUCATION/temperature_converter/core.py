"""
Полигон №2
"""

import os
import random

import temp_conv_list_formula as lf
import temp_conv_list_text as lt


def random_text():
    """Вызов случайной фразы"""
    rnd_sys = random.SystemRandom()
    return rnd_sys.choice(lt.RND_TEXT)


def cls():
    """Очистка консоли"""
    return os.system('cls' if os.name == 'nt' else 'clear')


def converter_module():
    """Модуль навигации конвертера"""
    cls()
    while True:
        temperature = 0
        convert_choice = 0
        print(lt.CONVERTER_MENU)
        cls()
        try:
            convert_choice = int(input('\nЧто конвертируем?\n'))
        except ValueError:
            print('Чел, используй цифры.')
        if convert_choice == 4:
            cls()
            break
        if convert_choice not in (1, 2, 3):
            print(lt.WRONG_ANSWER)
            print(random_text())
        if convert_choice in (1, 2, 3):
            temperature = float(input(lt.INFO_03))
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
    """Модуль навигации информации."""
    cls()
    while True:
        print(lt.INFORMATION_MENU)
        sub_choice_01 = int(input('\nЧто-то конкретное?\n'))
        if sub_choice_01 == 1:
            cls()
            print(lt.INFO_01)
        if sub_choice_01 == 2:
            cls()
            print(lt.INFO_02)
        if sub_choice_01 == 3:
            cls()
            break


def start_module():
    """Модуль навигации меню"""
    while True:
        cls()
        print(lt.MAIN_MENU)
        main_choice_01 = int(input('Приветствую! Что тебя интересует?\n'))
        if main_choice_01 == 1:
            info_module()
        if main_choice_01 == 2:
            converter_module()
        if main_choice_01 == 3:
            break


if __name__ == '__main__':
    start_module()
