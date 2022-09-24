"""
Домашняя работа. Лекция №2
"""

import random


# Task - 1
# Выяснить тип результата выражений.

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 2))

# Task - 2 & 3
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:

# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха',
# 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов.


some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for n, i in enumerate(some_list[:]):
    if i.isdigit():
        some_list.insert(some_list.index(i), '"')
        some_list.insert(some_list.index(i) + 1, '"')
        some_list[some_list.index(i)] = ('0' + i if len(i) < 2 else i)
    elif not i.isalpha():
        some_list.insert(some_list.index(i), '"')
        some_list.insert(some_list.index(i) + 1, '"')
        some_list[some_list.index(i)] = '{0}{2}{1}'.format(*i, 0)  # Уверен, что не правильно сделал.


print(some_list)

# в "05" часов "17" минут температура воздуха была "+05" градусов

print(f'{some_list[0]} {some_list[1]}{some_list[2]}{some_list[3]} {some_list[4]}'
      f' {some_list[5]}{some_list[6]}{some_list[7]} {some_list[8]} {some_list[9]}'
      f' {some_list[10]} {some_list[11]} {some_list[12]}{some_list[13]}{some_list[14]}'
      f' {some_list[15]}')

# Task - 4
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in name_list[:]:
    splitted_elements = i.split()
    print(f'Привет {splitted_elements[-1].title()}')

# Task - 5
# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку
# цена должна отображаться в виде <r> руб <kk> коп.
# (например «5 руб 04 коп.»)
# Подумать, как из цены получить рубли и копейки
# Как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп. или 00 коп.)
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [round(random.uniform(1.0, 25.0), 2) for _ in range(10, 20)]

print(price_list)

for i in price_list[:]:
    splt_price = str(i).split('.')
    print(f'{splt_price[0]} руб. {"0" + splt_price[1] if len(splt_price[1]) < 2 else splt_price[1]} коп.')