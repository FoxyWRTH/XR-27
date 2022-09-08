# Игра угадай число.
import random

while True:
    try:
        player_range_count = int(input('Введите диапазон чисел. \n'))
        player_try_count = int(input('Введите желаемое количество попыток. \n'))
        break
    except ValueError:
        print('Fuck You!')

pc_random_try = random.randrange(0, int(player_range_count))
# print(pc_random_try)

for i in range(player_try_count):
    player_try = input('Введите число \n')
    if player_try == 'exit' or player_try == 'выход':
        print('Победа достаётся только упорным!')
        exit()
    elif not player_try.isdigit():
        print(f'Вводи только целые числа. Кстати у тебя осталось {player_try_count - i - 1} попыток! ;)')
    elif int(player_try) == pc_random_try:
        print(f'Молодец, ты победил. Использовано попыток: {i}')
        break
    elif int(player_try) > pc_random_try:
        print(f'Ты ввел больше чем нужно, у тебя осталось {player_try_count - i - 1} попыток.')
    elif int(player_try) < pc_random_try:
        print(f'Ты ввел меньше чем нужно, у тебя осталось {player_try_count - i - 1} попыток.')
