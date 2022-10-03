"""
Домашняя работа. Лекция №5
"""

# Task - 1
# Написать генератор нечётных чисел от 1 до n (включительно)
# Используя ключевое слово yield.


def odd_generator_yield(max_n):
    """
    :param Максимальное число.
    :return набор нечётных чисел до максимального числа.
    """
    for i in range(1, max_n + 1):
        if i % 2 != 0:
            yield i


odd_list_yield = odd_generator_yield(10 ** 6)
print(max(odd_list_yield))

# Task - 2
# Решить задачу генерации нечётных чисел от 1 до n (включительно)
# Не используя ключевое слово yield.
MAX_N = 10 ** 6
odd_list = [i for i in range(1, MAX_N + 1) if i % 2 != 0]
print(max(odd_list))

# Task - 3
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors
# Необходимо вывести последние кортежи в виде: (<tutor>, None)
# Например:
# ('Станислав', None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '11А', '3В']


def union_generator(union_1, union_2):
    """
    :param union_1: 1 список.
    :param union_2: 2 список.
    :return кортежи из объединения списков.
    """
    len_1 = len(union_1)
    len_2 = len(union_2)
    if len_1 < len_2:
        for _ in range(len_2 - len_1):
            union_1.append(None)
    elif len_2 < len_1:
        for _ in range(len_1 - len_2):
            union_2.append(None)
    for index, element in enumerate(tutors):
        result = (element, klasses[index])
        yield result


generator_result = union_generator(tutors, klasses)
for i in generator_result:
    print(i)

# Task - 4.

# Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего
# Например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []

for i in range(1, len(some_list)):
    if some_list[i] > some_list[i - 1]:
        result_list.append(some_list[i])

print(result_list)

# Task - 5.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования
# в исходном списке, например:
# result = [23, 1, 3, 10, 4, 11]

source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(source)
result = [i for i in source if source.count(i) == 1]
print(result)
