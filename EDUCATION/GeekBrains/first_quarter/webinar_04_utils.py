"""
Модуль для вызова из термина. Задание вебинара №4.
"""

import sys
from webinar_04 import current_rates
from colorama import Fore, Style
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
