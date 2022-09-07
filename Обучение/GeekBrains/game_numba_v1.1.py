# Игра угадай число.
import random

player_try_count = input('Введите желаемое количество попыток. \n')
player_range_count = input('Введите диапазон чисел. \n')

while True:
    if player_try_count in ('exit', 'выход') or player_range_count in ('exit', 'выход'):
        exit()
    elif player_try_count.isdigit() and player_range_count.isdigit():
        break
    else:
        print('Введи целое число. И только его. Давай по новой...\n')
        player_try_count = input('Введите желаемое количество попыток. \n')
        player_range_count = input('Введите диапазон чисел. \n')

pc_random_try = random.randrange(0, int(player_range_count))
# print(pc_random_try)

for i in range(int(player_try_count)):
    player_try = input('Введите число \n')
    if player_try == 'exit' or player_try == 'выход':
        print('Победа достаётся только упорным!')
        exit()
    elif not player_try.isdigit():
        print(f'Вводи только целые числа. Кстати у тебя осталось {int(player_try_count) - i - 1} попыток! ;)')
        i = + 1
    elif int(player_try) == pc_random_try:
        print(f'Ты победил бля! Всего то за {i} попыток!')
        break
    elif int(player_try) > pc_random_try:
        print(f'Ты ввел больше чем нужно, у тебя осталось {int(player_try_count) - i - 1} попыток.')
        i = + 1
    elif int(player_try) < pc_random_try:
        print(f'Ты ввел меньше чем нужно, у тебя осталось {int(player_try_count) - i - 1} попыток.')
        i = + 1