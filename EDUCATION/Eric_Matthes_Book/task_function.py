"""
Задачи из книги. --Глава 8. Функции
"""

print('Task 1\n')

# Футболка. (8.3)
# напишите функцию make_shirt(), которая получает размер футболки и текст.
# Который должен быть напечатан на ней. Функция должна выводить сообщение с
# размером и текстом.

# Вызовите функцию с использованием позиционных аргументов.
# Вызовите функцию во второй раз с использованием именованных аргументов.


def make_shirt(value, text):
    """Just a primitive function"""
    return print(f'You ordered shirt with value: {value}, '
                 f'and want see text on shirt: "{text}"')


make_shirt('S', 'Fuck the World!')

print('\nTask 2\n')


# Большие футболки. (8.4)
# измените функцию make_shirt(), чтобы по умолчанию
# футболки имели размер L и на них выводился текст «I love Python».
# Создайте футболку с размером L и текстом по умолчанию, а также футболку
# любого размера с другим текстом.

def make_shirt_v2(text='I Love Python', value='L'):
    """Just a primitive function"""
    return print(f'You ordered shirt with value: {value}, '
                 f'and want see text on shirt: "{text}"')


make_shirt_v2()

print('\nTask 3\n')
