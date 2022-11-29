"""
Полигон №2
"""

import os
import subprocess
import time

import temp_conv_list_formula as lf
import temp_conv_list_text as lt
import temp_conv_list_event as ev


def cls():
    """Очистка консоли"""
    return subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


def input_celsius(temperature):
    """Конвертация Цельсий"""
    print(f'\nТемпература по Кельвину:'
          f' {round(lf.celsius_in_kelvin(temperature), 2)}K')
    print(f'Температура по Фаренгейту:'
          f' {round(lf.celsius_in_fahrenheit(temperature), 2)}°F')


def input_kelvin(temperature):
    """Конвертация Кельвин"""
    print(f'\nТемпература по Цельсию:'
          f' {round(lf.kelvin_in_celsius(temperature), 2)}°C')
    print(f'Температура по Фаренгейту:'
          f' {round(lf.kelvin_in_fahrenheit(temperature), 2)}°F')


def input_fahrenheit(temperature):
    """Конвертация Фаренгейт"""
    print(f'\nТемпература по Цельсию:'
          f' {round(lf.fahrenheit_in_celsius(temperature), 2)}°C')
    print(f'Температура по Кельвину:'
          f' {round(lf.fahrenheit_in_kelvin(temperature), 2)}K')


def wrong_answer():
    """Вывод сообщения при не корректном вводе."""
    cls()
    print(lt.WRONG_ANSWER)
    time.sleep(1)
    print(lt.random_text(lt.RND_TEXT_WRONG_ANSWER))
    time.sleep(1)
    ev.rnd_wrong_answer()
    time.sleep(1)
    cls()


def converter_module():
    """Модуль навигации конвертера"""
    cls()
    while True:
        temperature = 0
        print(lt.CONVERTER_MENU)
        convert_choice = input(f'\n{lt.random_text(lt.RND_INPUT_CONVERTER)}\n')
        if convert_choice == '4':
            cls()
            break
        if convert_choice in ('1', '2', '3'):
            cls()
            try:
                temperature = float(input(lt.INFO_03))
            except ValueError:
                wrong_answer()
                converter_module()
        if convert_choice == '1':  # Цельсий
            cls()
            input_celsius(temperature)
        elif convert_choice == '2':  # Кельвин
            cls()
            input_kelvin(temperature)
        elif convert_choice == '3':  # Фаренгейт
            cls()
            input_fahrenheit(temperature)
        else:
            wrong_answer()


def info_module():
    """Модуль навигации информации."""
    cls()
    while True:
        print(lt.INFORMATION_MENU)
        sub_choice_01 = input(f'\n{lt.random_text(lt.RND_INPUT_INFO)}\n')
        if sub_choice_01 == '3':
            cls()
            break
        if sub_choice_01 == '1':
            cls()
            print(lt.INFO_01)
        elif sub_choice_01 == '2':
            cls()
            print(lt.INFO_02)
        else:
            wrong_answer()


def start_module():
    """Модуль навигации меню"""
    cls()
    while True:
        print(lt.MAIN_MENU)
        main_choice_01 = input(f'{lt.random_text(lt.RND_INPUT_MAIN)}\n')
        if main_choice_01 == '3':
            cls()
            break
        if main_choice_01 == '1':
            info_module()
        elif main_choice_01 == '2':
            converter_module()
        else:
            wrong_answer()


if __name__ == '__main__':
    start_module()
