"""
Модуль для вызова из термина. Задание вебинара №4.
"""

import sys
from webinar_04 import current_rates
from colorama import Fore, Style

# Task - 4/5
# Написать свой модуль utils и перенести в него функцию currency_rates()
# из предыдущего задания. Создать скрипт, в котором импортировать этот модуль
# и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
# Доработать скрипт из предыдущего задания:
# теперь он должен работать и из консоли.

FAILURE_MESSAGE = 'Не задан параметр'

try:
    COMMAND = sys.argv[1]
except IndexError:
    print(FAILURE_MESSAGE)
else:
    if COMMAND == 'rate':
        try:
            NAME = sys.argv[2]
        except IndexError:
            print(FAILURE_MESSAGE)
        else:
            print(current_rates(NAME))
    elif COMMAND != 'rate':
        print(Fore.RED + 'Команда не найдена\n' + Fore.GREEN +
              'Для доступа к функционалу укажите '
              'первым параметром "rate", а вторым '
              'литерал валюты для конвертации.' + Style.RESET_ALL)
    else:
        print('Литерал валюты не найден.')
