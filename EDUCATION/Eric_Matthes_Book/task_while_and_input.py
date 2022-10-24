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
