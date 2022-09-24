import math
import random

# Задача 1.

some_list_1 = [112, 'Chaos', 'M882', 53, 77, ['Granula', 'Hope'], 'Storm', 'Lightning']
some_list_2 = ['Armageddon', 'Granula', 93, 23, ['Unicorn', 'Rainbow', 'Sun'], 'M882', 'Lightning']

result = []

for element in some_list_1:
    if element in some_list_2:
        result.append(element)

print(result, 'result_v1')

# Иное исполнение Задачи 1:
result_v2 = [i for i in some_list_1 if i in some_list_2]
# Берём переменную, запускаем цикл, выставляем условие.
# ЭТО ГЕНЕРАТОР!
print(result_v2, 'result_v2')

# Задача 2.

some_generate_list = [random.randint(-10, 10) for _ in range(1, 20)]
print(some_generate_list)

upd_generate_list = []

for i in some_generate_list:
    if i % 3 == 0 and i % 4 != 0 and i > 0:
        upd_generate_list.append(i)

print(upd_generate_list)

# Иной вариант задачи 2:
result_v3 = [i for i in some_generate_list if i > 0 and i % 3 == 0 and i % 4 != 0]
print(result_v3, 'Result_v3')

# Задача 3.

another_list = [1, -3, 4, 32, 12, -122, 43]


def editing_numbers(some_list):
    another_list_upd = some_list.copy()
    result_2 = []
    for i in another_list_upd:
        if i > 0:
            result_2.append(round(math.sqrt(i), 4))
        else:
            result_2.append(i)
    return result_2


print(another_list, 'LIST_NUMBA_1')
print(editing_numbers(another_list), 'LIST NUMBA_2_COPY')


# Иной способ задачи 3:

def editing_numbers_v2():
    resurecta = [math.sqrt(i) for i in another_list if i > 0]
    return resurecta


def editing_numbers_v3():
    resurecta = [math.sqrt(i) if i > 0 else i for i in another_list]
    return resurecta


print(editing_numbers(another_list), 'RESURECTA! ГЕНЕРАТОР')
print(editing_numbers(another_list), 'RESURECTA! ТЕРНАРНЫЙ ОПЕРАТОР + ГЕНЕРАТОР')


# Задача 4.

def task_4(elementus):
    if elementus < 1 or elementus > 100:
        raise ValueError('Not in Range 1-100')
    if elementus == 13:
        raise ValueError('Oh fuck!')
    return elementus ** 2


print(task_4(random.randint(1, 100)))

# Иной способ задачи 4:
