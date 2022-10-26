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


# Названия городов (8.6)
# напишите функцию city_country(), которая получает название города и страну.
# Функция должна возвращать строку в формате "Santiago, Chile".
# Вызовите свою функцию по крайней мере для трех пар «город — страна»
# и выведите возвращенное значение.

def city_country(city, country):
    """Just another function to lern"""
    return print(f'{city} {country}')


COUNTER = 0
while COUNTER != 3:
    city_country(input('Enter city, please\n'),
                 input('Enter country please\n'))
    COUNTER += 1
    print()

print('\nTask 4\n')


# Альбом
# напишите функцию make_album(), которая строит словарь с описанием музыкального
# альбома. Функция должна получать имя исполнителя и название альбома и
# возвращать словарь, содержащий эти два вида информации. Используйте функцию
# для создания трех словарей, представляющих разные альбомы. Выведите все
# возвращаемые значения, чтобы показать, что информация правильно сохраняется
# во всех трех словарях.

# Добавьте в make_album() дополнительный параметр для сохранения количества
# дорожек в альбоме, имеющий значение по умолчанию None. Если в строку вызова
# включено значение количества дорожек, добавьте это значение в словарь альбома.
# Создайте как минимум один новый вызов функции с передачей количества дорожек
# в альбоме.

def make_album(name_artist, name_album, tracks=None):
    """Just function... Artist's... bla... bla..."""
    if tracks:
        result = {f'Artist Name: {name_artist} | '
                  f'Album Name: {name_album} | '
                  f'Track {tracks}'}
    else:
        result = {f'Artist Name: {name_artist} | '
                  f'Album Name: {name_album}'}
    return result


COUNTER = 0
while COUNTER != 3:
    print(make_album(input('Enter name of Artist\n'),
                     input('Enter name of Album\n'),
                     input('Enter count tracks\n')))
    COUNTER += 1

print('\nTask 5\n')

# Сообщения
# создайте список с серией коротких сообщений.
# Передайте список функции show_messages()
# которая выводит текст каждого сообщения в списке.

message_list = ['Stupid Fox', 'Lazy Fox', 'Coward Fox', 'Unhappy Fox']


def show_messages(messages):
    """Show messages in input list"""
    for i in messages:
        print(f'You are: {i}')


show_messages(message_list)

print('\nTask 6\n')

# Отправка сообщений.
# Напишите функцию send_messages(), которая выводит каждое сообщение и
# перемещает его в новый список с именем sent_messages.
# После вызова функции выведите оба списка и убедитесь в том,
# что перемещение прошло успешно.

message_list = ['You will be OK Foxy', 'Do not give up!']
sent_messages = []


def func_send_messages(list_of_message, sent_message):
    """Show messages in input list
    and send it to another list"""
    for i in list_of_message:
        print(f'Message sent: {i}')
    while message_list:
        popy = message_list.pop()
        print(f'Sending message: {popy}')
        sent_message.append(popy)


func_send_messages(message_list, sent_messages)
print()
print(f'message_list: {message_list}')
print(f'sent_messages: {sent_messages}')

print('\nTask 7\n')

# Архивированные сообщения
# Вызовите функцию send_messages() для копии списка сообщений.
# После вызова функции выведите оба списка и убедитесь в том, что в исходном
# списке остались все сообщения.

list_01 = [1, 2, 3, 4, 5, 6, 7]
list_02 = []


def move_elements(list_out, list_in):
    """Move elements in list_out to list_in"""
    while list_out:
        temp = list_out.pop()
        print(temp)
        list_in.append(temp)


move_elements(list_01[:], list_02)  # [:] - создаёт копию списка для работы.

print(list_01)
print(list_02)

print('\nTask 8\n')


# Сэндвичи (8.12)
# напишите функцию, которая получает список компонентов сэндвича.
# Функция должна иметь один параметр для любого количества значений, переданных
# при вызове функции, и выводить описание заказанного сэндвича. Вызовите функцию
# три раза с разным количеством аргументов.


def sandwich(*args):
    """Build sandwich"""
    print('You want sandwich with:')
    return args


print(sandwich('bread', 'meat', 'sous', 8))
print(sandwich('bread', 'potato', 'sous', 12))
print(sandwich('bread', 'meat', 'human', 23))

print('\nTask 9\n')


# Профиль. (8.13)
# Создайте собственный профиль вызовом build_profile(),
# укажите имя, фамилию и три другие пары «ключ-значение» для вашего описания.

def user_profile(first_name, last_name, **kwargs):
    """Build Profile"""
    kwargs['Name'] = first_name
    kwargs['Family'] = last_name
    return kwargs


print(user_profile('Foxy', 'WRTH',
                   Location='Orenburg',
                   Status='In shit',
                   Plan='Change Strategy'))

print('\nTask 10\n')


# Автомобили. (8.14)
# напишите функцию для сохранения информации об автомобиле в словаре.
# Функция всегда должна возвращать производителя и название модели, но при этом
# она может получать произвольное количество именованных аргументов.
# Вызовите функцию с передачей обязательной информации и еще двух пар
# «имя-значение» (например, цвет и комплектация).
# Ваша функция должна работать для вызовов следующего вида:

# car = make_car('subaru', 'outback', color='blue', tow_package=True) Вот так.

# Выведите возвращаемый словарь и убедитесь в том,
# что вся информация была сохранена правильно.

def car_func(car_name, car_type, **kwargs):
    """Another function to lern..."""
    return car_name, car_type, kwargs


print(car_func('Subaru', 'Transformer',
               color='Black',
               weight='High'))
