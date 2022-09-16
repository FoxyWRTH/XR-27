# Task - 1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в
# секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях:
# <d> дн <h> час <m> мин <s> сек.

time_set = int(input())

days = time_set // 86400
hours = time_set // 3600 % 24
minutes = time_set // 60 % 60
seconds = time_set % 60

if days < 0:
    pass
elif days > 0:
    print(f'{days} дн {hours} час {minutes} мин {seconds} cек')
elif hours < 0:
    pass
elif hours > 0:
    print(f'{hours} час {minutes} мин {seconds} cек')
elif minutes < 0:
    pass
elif minutes > 0:
    print(f'{minutes} мин {seconds} cек')
else:
    print(f'{seconds} cек')

# Task - 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X): Вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в
# сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции! К
# каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7. * Решить задачу под пунктом b, не создавая новый список.

some_list = [i ** 3 for i in range(1, 1001, 2)]

summa_1 = 0
summa_2 = 0

for source in some_list[:]:
    memory_cell = source
    sum_source = 0
    while source != 0:
        sum_source = sum_source + source % 10
        source = source // 10
    some_list.pop(source)
    some_list.append(memory_cell + 17)
    if sum_source % 7 == 0:
        summa_1 += memory_cell

for source in some_list[:]:
    memory_cell = source
    sum_source = 0
    while source != 0:
        sum_source = sum_source + source % 10
        source = source // 10
    if sum_source % 7 == 0:
        summa_2 += memory_cell

print(some_list)
print(summa_1)
print(summa_2)

# Task - 3
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент.
# 2 процента.
# 3 процента.
# 6 процентов.
# 100 процентов.

percent = [i for i in range(1, 101)]

for i in percent:
    if 11 <= i <= 14:
        print(f'{i} Процентов.')
    elif i % 10 == 1:
        print(f'{i} Процент.')
    elif 2 <= i % 10 <= 4:
        print(f'{i} Процента.')
    elif 5 <= i % 10 <= 9 or i % 10 == 0:
        print(f'{i} Процентов.')
