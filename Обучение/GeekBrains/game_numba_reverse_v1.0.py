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

correction = None  # Флаг корректировки содержится тут.
generate_memory = None  # Короткая, временная память ответа.
pc_generate_number = random.randrange(1, int(player_range))  # Первичная генерация числа для угадывания.

generate_memory_long_1 = int(1)  # Долгая, временная память ответа нижнего предела.
generate_memory_long_2 = int(player_range)  # Долгая, временная память ответа верхнего предела.
pc_try_end = 1

for i in range(1, int(pc_try_count) + 2):
    #  Блок корректировки.
    if correction == '>':
        generate_memory_long_1 = generate_memory
        pc_generate_number = random.randrange(int(generate_memory_long_1) + 1, int(generate_memory_long_2))
    elif correction == '<':
        generate_memory_long_2 = generate_memory
        pc_generate_number = random.randrange(generate_memory_long_1, int(generate_memory_long_2)) - 1

    #  Блок сравнения.
    if int(pc_generate_number) == int(player_number):
        print(f'Компьютер полагает что ваше число: {pc_generate_number}')
        print(f'И это верное предположение. Попыток использовано компьютером: {i}')
        exit()
    elif correction == 'exit':
        print('Что - то пошло не так?')
        exit()
    elif int(pc_try_end) > int(pc_try_count):
        print('Компьютер, истратив все доступные ему попытки проиграл. Гордая победа Человека над машиной!')
        exit()
    elif pc_generate_number != player_number:
        print(f'Компьютер полагает что ваше число: {pc_generate_number}')
        print(f'Если вы вдруг забыли, вы загадали {player_number}')
        print(f'Осталось попыток: {int(pc_try_count) - i}')
        print('Внесите корректировку, используйте "<" и ">" для корректировки диапазона.')
        correction = input()  # Внесение флага корректировки.
        generate_memory = pc_generate_number  # Первичное запоминания сгенерированного числа.
        pc_try_end += 1
