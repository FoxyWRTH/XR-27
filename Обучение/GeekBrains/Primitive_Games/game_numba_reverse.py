# Игра, угадай число. Со стороны компьютера.
import random


def game_numba_reverse():
    while True:
        try:
            player_range = int(input('Введи диапазон. Используйте только цифры.\n'))
            pc_try_count = int(input('Сколько попыток будет у компьютера? Используйте только цифры.\n'))
            player_number = int(input('Введи число которое будет отгадывать компьютер. Используйте только цифры.\n'))
            break
        except ValueError:
            print('Используйте только целые цифры.')

    min_number = 1
    max_number = int(player_range)
    try_count = 1

    for i in range(1, pc_try_count + 1):
        pc_try_catch = random.randint(min_number, max_number)
        print(f'Компьютер полагает что ваше число: {pc_try_catch}')
        print(f'Если вы вдруг забыли, вы загадали {player_number}')
        print(f'Осталось попыток: {pc_try_count - i}')
        correction = input('Введите корректировку\n')

        if int(player_number) == pc_try_catch:
            print(f'Компьютер победил. Попыток использовано компьютером для отгадывания числа: {i}')
            exit()
        elif try_count == pc_try_count:
            print('Компьютер, истратив все доступные ему попытки проиграл. Гордая победа Человека над машиной!')
            exit()
        elif correction == '>':
            min_number = pc_try_catch + 1
        elif correction == '<':
            max_number = pc_try_catch - 1
        try_count += 1


if __name__ == '__main__':
    game_numba_reverse()
