"""
Задачи на Stepik
"""
import numpy as np

# На вход программе подается последовательность слов, каждое слово на
# отдельной строке. Концом последовательности является слово «КОНЕЦ» (без
# кавычек).
#
# Напишите программу, которая выводит члены данной последовательности.

words = input()

while words != 'КОНЕЦ':
    print(words)
    words = input()

# На вход программе подается последовательность слов, каждое слово на
# отдельной строке. Концом последовательности является слово «КОНЕЦ» или
# «конец» (большими или маленькими буквами, без кавычек).
#
# Напишите программу, которая выводит члены данной последовательности.

words = input()

while words.lower() != 'конец':
    print(words)
    words = input()

# На вход программе подается последовательность слов, каждое слово на
# отдельной строке. Концом последовательности является одно из трех слов:
# «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
#
# Напишите программу, которая выводит общее количество членов
# данной последовательности.

words = input()
count = 0

while words.lower() not in ('стоп', 'хватит', 'достаточно'):
    count += 1
    words = input()

print(count)

# На вход программе подается последовательность целых чисел делящихся на 77,
# каждое число на отдельной строке. Концом последовательности является любое
# число не делящееся на 77.
#
# Напишите программу, которая выводит члены данной последовательности.

numba = int(input())

while True:
    if numba != numba % 7 == 0:
        print(numba)
        numba = int(input())
    elif numba == 0:
        print(numba)
        break
    else:
        break

# На вход программе подается последовательность целых чисел, каждое число на
# отдельной строке. Концом последовательности является любое отрицательное
# число.
#
# Напишите программу, которая выводит сумму всех членов
# данной последовательности.

numba = int(input())
count = 0

while 0 <= numba <= 5:
    if numba == 5:
        count += 1
    numba = int(input())

print(count)

# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его
# услуги обойдутся недешево, к тому же ведьмак не принимает купюры,
# он принимает только чеканные монеты. В мире ведьмака существуют монеты с
# номиналами 1, \, 5, \, 10, \, 251,5,10,25.
#
# Напишите программу, которая определяет какое минимальное количество
# чеканных монет нужно заплатить ведьмаку.

reward = int(input())
counter = 0

while reward >= 25:
    reward = reward - 25
    counter += 1
while reward >= 10:
    reward = reward - 10
    counter += 1
while reward >= 5:
    reward = reward - 5
    counter += 1
while reward >= 1:
    reward = reward - 1
    counter += 1

print(counter)

# Поиск цифры в целом числе.

numba = 1171125
has_seven = False

while numba != 0:
    last_digit = numba % 10
    if last_digit == 7:
        has_seven = True
    numba = numba // 10

if has_seven == True:
    print('Yes')
else:
    print('No')

# Дано натуральное число.

# Напишите программу, которая выводит его цифры в столбик в обратном порядке.

number = int(input())

while number != 0:
    last_number = number % 10
    print(last_number)
    number = number // 10

# Дано натуральное число.
#
# Напишите программу, которая меняет порядок цифр числа на обратный.

number = int(input())
number_reverse = ''

while number != 0:
    last_number = number % 10
    number_reverse += str(last_number)
    number = number // 10

print(int(number_reverse))

# Дано натуральное число.
#
# Напишите программу, которая меняет порядок цифр числа на обратный.
# БОЛЕЕ УДАЧНЫЙ ВАРИАНТ:

number = int(input())
while number != 0:
    print(number % 10, end='')
    number = number // 10

# Дано натуральное число.
#
# Напишите программу, которая определяет его максимальную и минимальную цифры.

number = int(input())
sorting = []
while number != 0:
    last_number = number % 10
    sorting.append(last_number)
    number = number // 10

print(f'Максимальная цифра равна {max(sorting)}')
print(f'Минимальная цифра равна {min(sorting)}')

# Дано натуральное число.
#
# Напишите программу, которая вычисляет:
#
#     сумму его цифр;
#     количество цифр в нем;
#     произведение его цифр;
#     среднее арифметическое его цифр;
#     его первую цифру;
#     сумму его первой и последней цифры.

input_number = int(input())

item_list = []
while input_number != 0:
    last_number = input_number % 10
    item_list.append(last_number)
    input_number = input_number // 10

print(sum(item_list))  # сумму его цифр;
print(len(item_list))  # количество цифр в нем;
print(np.prod(item_list))  # произведение его цифр;
print(np.mean(item_list))  # среднее арифметическое его цифр;
print(item_list[-1])  # его первую цифру;
print(item_list[-1] + item_list[0])  # сумму его первой и последней цифры.

# Дано натуральное число.
#
# Напишите программу, которая определяет его вторую (с начала) цифру.

input_number = int(input())

item_list = []
while input_number != 0:
    last_number = input_number % 10
    item_list.append(last_number)
    input_number = input_number // 10

item_list.reverse()

print(item_list[1])

# Ультра короткий вариант:

print(input()[1])

# Дано натуральное число.
#
# Напишите программу, которая определяет,
# состоит ли указанное число из одинаковых цифр.

