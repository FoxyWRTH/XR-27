# Игра угадай число.
import random
from colorama import *

player_try_count = input(Fore.GREEN + 'Введите желаемое количество попыток. \n' + Style.RESET_ALL)
player_range_count = input(Fore.GREEN + 'Введите диапазон чисел. \n' + Style.RESET_ALL)

while True:
    if player_try_count == 'exit' or player_try_count == 'выход':
        exit()
    elif player_range_count == 'exit' or player_range_count == 'выход':
        exit()
    elif player_try_count.isdigit() and player_range_count.isdigit():
        break
    else:
        print(Fore.RED + 'Введи целое число. И только его. Давай по новой...\n' + Style.RESET_ALL)
        player_try_count = input(Fore.GREEN + 'Введите желаемое количество попыток. \n' + Style.RESET_ALL)
        player_range_count = input(Fore.GREEN + 'Введите диапазон чисел. \n' + Style.RESET_ALL)

pc_random_try = random.randrange(0, int(player_range_count))
# print(pc_random_try)

for i in range(int(player_try_count)):
    player_try = input('Введите число \n')
    if player_try == 'exit' or player_try == 'выход':
        print(Fore.CYAN + 'Победа достаётся только упорным!' + Style.RESET_ALL)
        exit()
    elif not player_try.isdigit():
        print(Fore.RED + 'Вводи только целые числа. Кстати у тебя осталось ' + Style.RESET_ALL + Fore.YELLOW
              + f'{int(player_try_count) - i - 1}' + Style.RESET_ALL + Fore.RED + ' попыток! ;)' + Style.RESET_ALL)
        i = + 1
    elif int(player_try) == pc_random_try:
        print(Fore.CYAN + f'Ты победил бля! Всего то за {i} попыток!' + Style.RESET_ALL)
        break
    elif int(player_try) > pc_random_try:
        print(Fore.GREEN + f'Ты ввел больше чем нужно, у тебя осталось ' + Style.RESET_ALL +
              Fore.YELLOW + f'{int(player_try_count) - i - 1}' + Style.RESET_ALL +
              Fore.GREEN + ' попыток.' + Style.RESET_ALL)
        i = + 1
    elif int(player_try) < pc_random_try:
        print(Fore.GREEN + f'Ты ввел меньше чем нужно, у тебя осталось ' + Style.RESET_ALL +
              Fore.YELLOW + f'{int(player_try_count) - i - 1}' + Style.RESET_ALL +
              Fore.GREEN + ' попыток.' + Style.RESET_ALL)
        i = + 1
