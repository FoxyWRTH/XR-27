"""
Задачи из книги. --Глава 9. Модули
"""
import random
import statistics


# Кубики (9.13)
# Создайте класс Die с одним атрибутом sides, который имеет значение
# по умолчанию 6. Напишите метод roll_die() для вывода случайного числа
# от 1 до количества граней на кубике. Создайте экземпляр, представляющий
# 6-гранный кубик, и смоделируйте 10 бросков.

# Создайте экземпляры, представляющие 10- и 20-гранный кубик.
# Смоделируйте 10 бросков каждого кубика.

class Die():
    """Класс кубика"""

    def __init__(self, roll_sides_6=6, roll_sides_10=10, roll_sides_20=20):
        """Инициализация аттрибутов"""
        self.sides_6 = roll_sides_6
        self.sides_10 = roll_sides_10
        self.sides_20 = roll_sides_20

    def roll_die_6(self):
        """Бросок кубика"""
        roll_6 = random.randint(1, self.sides_6)
        print(f'Roll cube 6... and we get... {roll_6}')

    def roll_die_10(self):
        """Бросок кубика"""
        roll_10 = random.randint(1, self.sides_10)
        print(f'Roll cube 10... and we get... {roll_10}')

    def roll_die_20(self):
        """Бросок кубика"""
        roll_20 = random.randint(1, self.sides_20)
        print(f'Roll cube 20... and we get... {roll_20}')


cube_6 = Die()
cube_10 = Die()
cube_20 = Die()

for _ in range(0, 3):
    cube_6.roll_die_6()

for _ in range(0, 3):
    cube_10.roll_die_10()

for _ in range(0, 3):
    cube_20.roll_die_20()

# Лотерея. (9.14)
# Создайте список или кортеж, содержащий серию из 10 чисел и 5 букв.
# Случайным образом выберите 4 числа или буквы из списка.
# Выведите сообщение о том, что билет, содержащий эту комбинацию из четырех
# цифр или букв, является выигрышным.

another_element = [84, 'V9', 43, 'L2', 32, 'S14', 54, 'K5', 'D5', 43]
element_list = [84, 'V9', 43, 'L2', 32, 'S14', 54, 'K5', 'D5', 43]
win_list = []

for i in range(0, 5):
    win_list.append(random.choice(element_list))

print(f'\n{win_list}'
      f'\nSo, if your ticket have that combination you are the WINNER!')

# Анализ лотереи. (9.15)
# Напишите цикл, который проверяет, насколько сложно выиграть в
# смоделированной вами лотерее. Создайте список или кортеж с именем my_ticket.
# Напишите цикл, который продолжает генерировать комбинации до тех пор, пока
# не выпадет выигрышная комбинация. Выведите сообщение с информацией о том,
# сколько выполнений цикла понадобилось для получения выигрышной комбинации.

TRY_COUNT = []

for _ in range(0, 10):
    COUNTER = 0
    while True:
        my_ticket = []
        for i in range(0, 5):
            my_ticket.append(random.choice(element_list))
        COUNTER += 1
        if my_ticket == win_list:
            break
        my_ticket.clear()
    TRY_COUNT.append(COUNTER)

print(f'\nКоличество элементов для подбора: {len(win_list)}\n'
      f'Количество замеров: {len(TRY_COUNT)}\n'
      f'Среднее количество попыток: {round(statistics.mean(TRY_COUNT))}'
      f'\n'
      f'Список затраченных попыток: \n{TRY_COUNT}\n'
      f'Общее количество попыток: {sum(TRY_COUNT)}')
