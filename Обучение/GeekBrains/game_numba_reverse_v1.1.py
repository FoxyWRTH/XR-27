# Игра, угадай число. Со стороны компьютера.

import random

# Ниже — Врата. Они отсекают возможность внести что-либо, кроме цифр.
player_range = input('Введи диапазон. Используйте только цифры.\n')
player_number = input('Введи своё число которое будет пытаться отгадать компьютер. Используйте только цифры.\n')
pc_try_count = input('Сколько попыток будет у компьютера? Используйте только цифры.\n')

while True:
    if player_number in ('exit', 'выход') or pc_try_count in ('exit', 'выход') or player_range in ('exit', 'выход'):
        exit()
    elif player_range.isdigit() and player_number.isdigit() and pc_try_count.isdigit():
        break
    else:
        print('Используйте только целые цифры.')
        player_range = input('Введи диапазон. Используйте только цифры.\n')
        player_number = input('Введи своё число которое будет пытаться отгадать компьютер. Используйте только цифры.\n')
        pc_try_count = input('Сколько попыток будет у компьютера? Используйте только цифры.\n')

min_number = 1
max_number = int(player_range)
try_count = 1

for i in range(1, int(pc_try_count) + 1):
    pc_try_catch = random.randint(min_number, max_number)
    print(f'Компьютер полагает что ваше число: {pc_try_catch}')
    print(f'Если вы вдруг забыли, вы загадали {player_number}')
    print(f'Осталось попыток: {int(pc_try_count) - i}')
    correction = input('Введите корректировку\n')

    if int(player_number) == int(pc_try_catch):
        print(f'Компьютер победил. Попыток использовано компьютером для отгадывания числа: {i}')
        exit()
    elif try_count == int(pc_try_count):
        print('Компьютер, истратив все доступные ему попытки проиграл. Гордая победа Человека над машиной!')
        exit()
    elif correction == '>':
        min_number = pc_try_catch + 1
    elif correction == '<':
        max_number = pc_try_catch - 1
    try_count += 1
