"""
Задачи из книги. --Глава 7. Цикл While и функция input()
"""

print('Task 1\n')

# Прокат машин. (7.1)
# Напишите программу, которая спрашивает у пользователя.
# Какую машину он бы хотел взять напрокат.
# Выведите сообщение с введенными данными.
# (например, "Let me see if I can find you a Subaru").

question = input('Please, tell me what car you want?\n')
print(f'Let me see if I can find you a {question}...')

print('\nTask 2\n')

# Заказ стола. (7.2)
# Напишите программу, которая спрашивает у пользователя.
# На сколько мест он хочет забронировать стол в ресторане.
# Если введенное число больше 8,
# выведите сообщение о том, что пользователю придется подождать.
# В противном случае сообщите, что стол готов.

places = int(input('Please tell me, how many people will come?\n'))

if places > 8:
    print('Sorry, but you need to wait until tables are free.')
else:
    print('Alright, table are ready!')

print('\nTask 3\n')

# Числа, кратные 10. (7.3)
# Запросите у пользователя число и сообщите, кратно оно 10 или нет.

ask_number = int(input('Enter the number, please.\n'))

if ask_number % 10 == 0:
    print('Yes, it OK.')
else:
    print("No, it's not right")

print('\nTask 4\n')

# Топпинг для пиццы. (7.4)
# Напишите цикл, который предлагает пользователю вводить дополнения для пиццы
# до тех пор, пока не будет введено значение 'quit'.
# При вводе каждого дополнения выведите сообщение о том,
# что это дополнение включено в заказ.

topping_list = []
WELCOME_ASKING = 'Hello, what topping you want see in your pizza?\n' \
                 '"Notice: write "enough" to stop adding toppings"\n'
while True:
    asking = input(WELCOME_ASKING)
    if asking.lower() == 'enough':
        print('All right! Your pizza will be with you soon! Enjoy your meal!')
        break
    topping_list.append(asking)
    print(f'{asking.title()} added to your pizza!')
    WELCOME_ASKING = 'Something else?\n'

print('\nTask 5\n')

# Билеты в кино. (7.5)
# кинотеатр установил несколько вариантов цены на билеты
# в зависимости от возраста посетителя.
# Для посетителей младше 3 лет билет бесплатный;
# в возрасте от 3 до 12 билет стоит $10;
# наконец, если возраст посетителя больше 12, билет стоит $15.
# Напишите цикл, который предлагает пользователю ввести возраст
# и выводит цену билета.

WELCOME_SPEECH = "Hello! Tell me how old are you and," \
                 " I'll tell you the ticket price!\n" \
                 "'Notice: Use only numbers!\n" \
                 "'Notice: You can quit program. Just write '911'\n"

while True:
    age = int(input(WELCOME_SPEECH))
    if age == 911:
        print('Ok... Alright...')
        break
    if age < 3:
        print('Beautiful! You can go for free!')
    elif 3 <= age <= 12:
        print('For you my dear friend, ticket will cost 10$')
    elif age > 12:
        print('For you my dear friend, ticket will cost 15$')
    else:
        print('Something wrong, check the number what you write...')
    WELCOME_SPEECH = 'Something else?\n'

print('\nTask 6\n')

# Сэндвичи. (7.8)
# Создайте список с именем sandwich_orders, заполните его названиями различных
# видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле
# переберите элементы первого списка и выведите сообщение для каждого элемента
# (например, «I made your tuna sandwich»). После этого каждый сэндвич из первого
# списка перемещается в список finished_sandwiches. После того как все элементы
# первого списка будут обработаны, выведите сообщение с перечислением
# всех изготовленных сэндвичей.

sandwich_orders = ['tanos', 'eros', 'juli', 'bread_and_meat']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'«I made your "{current_sandwich.title()}" sandwich»')
    finished_sandwiches.append(current_sandwich)

for i in finished_sandwiches:
    print(f'Your "{i.title()}" sandwich is ready!')

print('\nTask 7\n')

# Без пастрами (7.9)
# используя список sandwich_orders из упражнения 7.8,
# проследите за тем, чтобы значение 'pastrami' встречалось в списке как
# минимум три раза. Добавьте в начало программы код для вывода сообщения о
# том, что пастрами больше нет, и напишите цикл while для удаления всех
# вхождений 'pastrami' из sandwich_orders. Убедитесь в том, что в
# finished_sandwiches значение 'pastrami' не встречается ни одного раза.

sandwich_orders_2 = ['tanos', 'eros', 'juli', 'bread_and_meat', 'eros',
                     'tanos', 'eros', 'juli', 'eros', 'eros']

print('"Eros" sandwich is over. bruh...')

while 'eros' in sandwich_orders_2:
    sandwich_orders_2.remove('eros')

print('Now all I have to do is...')

for i in sandwich_orders_2:
    print(i.title(), end=' - ')

print('\nTask 8\n')

# Отпуск мечты. (7.10)
# Напишите программу, которая опрашивает пользователей, где бы они
# хотели провести отпуск. Включите блок кода для вывода результатов опроса.
# Я сделал по другому. Потому что у меня нет сил мечтать за других...

responses = {}
INTERVIEW = True

while INTERVIEW:
    key = input('Enter you Name, unit.\n')
    while key == '':
        key = input('I repeat, enter you Name, unit.\n')
    value = input('Enter your Data, unit.\n')
    while value == '':
        value = input('I repeat, Enter your Data, unit.\n')

    responses[key] = value  # Вот так выглядит присвоение к словарю. Запомни.

    repeat = input('Continue, or stop?\n')
    if repeat == 'stop':
        INTERVIEW = False

for key, value in responses.items():
    print(f'Key - {key}, Value - {value}')

print('\nTask 9\n')
