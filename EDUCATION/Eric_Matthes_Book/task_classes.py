"""
Задачи из книги. --Глава 9. Классы
"""
import random


class Dog():  # Определение класса и присваивание имени "Dog".
    """Простая модель собаки.
    Всегда пишутся с большой буквы."""

    def __init__(self, name, age):  # Специальный метод "__init__"
        """Инициализация атрибутов класса, name и age.
        --Атрибут 'self' всегда идёт перед остальными атрибутами.
        --Любая переменная с префиксом self доступна для каждого метода в
        классе и вы также сможете обращаться к этим переменным в каждом
        экземпляре, созданном на основе класса."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится"""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Собака перекатывается"""
        print(f'{self.name} rolled over!')


my_dog = Dog('Fargus', 17)
your_dog = Dog('Alice', 8)

print(f'Name of my dog is {my_dog.name}')
print(f'My dog is {my_dog.age}, years old!')
my_dog.sit()

print(f'Name of your dog is {your_dog.name}')
print(f'Your dog is {your_dog.age}, years old!')
your_dog.roll_over()

print('\nTask 1\n')


# Ресторан
# Создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен
# содержать два атрибута: restaurant_name и cuisine_type.
# Создайте метод describe_restaurant(),
# который выводит два атрибута.
# И метод open_restaurant(),
# который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant.
# Выведите два атрибута по отдельности, затем вызовите оба метода.

class Restaurant():
    """Модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация атрибутов"""
        self.name = restaurant_name
        self.kitchen_type = cuisine_type

    def describe_restaurant(self):
        """Вывод информации о ресторане"""
        print(f'Name of this restaurant: {self.name}\n'
              f'Kitchen type: {self.kitchen_type}')

    def open_restaurant(self):
        """Вывод сообщения о том что ресторан открыт."""
        print(f'Restaurant {self.name} is OPEN!')


build_1 = Restaurant('MX-23', 'Type-9')

build_1.open_restaurant()
build_1.describe_restaurant()

build_2 = Restaurant('MX-34', 'Type-2')

build_2.open_restaurant()
build_2.describe_restaurant()

print('\nTask 2\n')


# Пользователи
# Создайте класс с именем User. Создайте два атрибута first_name и last_name,
# а затем еще несколько атрибутов, которые обычно хранятся в профиле
# пользователя. Напишите метод describe_user(), который выводит сводку с
# информацией о пользователе. Создайте еще один метод greet_user() для вывода
# персонального приветствия для пользователя.

class User():
    """Класс пользователь"""

    def __init__(self, first_name, last_name, middle_name=''):
        """Имя, фамилия, кличка"""
        self.f_name = first_name
        self.l_name = last_name
        self.m_name = middle_name

    def describe_user(self):
        """Инфо о пользователе"""
        if self.m_name:
            return (f'Name of person:'
                    f' {self.f_name} {self.l_name} "{self.m_name}"')
        return f'Name of person: {self.f_name} {self.l_name}'

    def greet_user(self):
        """Приветствие пользователя"""
        if self.m_name:
            return (f'Hello and welcome '
                    f'{self.f_name} {self.l_name} "{self.m_name}" '
                    f'glad to see you! Make yourself comfortable.')
        return (f'Hello and welcome {self.f_name} {self.l_name} '
                f'glad to see you! Make yourself comfortable.')


some_person_01 = User('Mike', 'Artek', 'Luxor')
print(some_person_01.greet_user())
print(some_person_01.describe_user())

some_person_02 = User('Alexander', 'Nevskii')
print(some_person_02.greet_user())
print(some_person_02.describe_user())

print('\nTask ~3\n')


class KillBot():
    """Just another human friend!"""

    def __init__(self, model, description, name):
        """Initialization"""
        self.bot_model = model
        self.bot_name = name
        self.bot_description = description
        self.victims = 0
        self.nuclear_victims = 0

    def description(self):
        """Bot Greetings"""
        return f'Look of this brilliant bot! Hm, model {self.bot_model}. ' \
               f'And his name... Ah, here it is, {self.bot_name}. '

    def use_volcan_weapon(self):
        """Just kill them"""
        killed_people = int(random.randint(1, 50))
        self.victims += killed_people
        return f'{self.bot_model}, kill {killed_people}'

    def launch_nuclear(self):
        """Launching tactical nuclear rocket"""
        nuclear_kill = int(random.randint(400, 1000))
        self.nuclear_victims = nuclear_kill
        return f'{self.bot_model} launching N-rocket, and kill {nuclear_kill}'


model_01 = KillBot('XR-12', 'Human Friend!', 'Roxy')

print(model_01.description())
print(f'Hm, he not kill... Kill count... {model_01.victims}, nuclear kill '
      f'count... {model_01.nuclear_victims}')
print(f'Ok, i just push this button... And... He, comes to live. '
      f'Good morning {model_01.bot_model}. Do you want be human friend?')
print(model_01.use_volcan_weapon())
print(model_01.launch_nuclear())
print(f'Ah! Brilliant results! now let se the count of kills! '
      f'Kill count... {model_01.victims}, '
      f'nuclear kill count... {model_01.nuclear_victims}')
print()


class SubKillBot(KillBot):
    """Little sub bot"""

    def __init__(self, model, description, name):
        """Initialization"""
        super().__init__(model, description, name)
        self.os_system = 'sub_os_7'

    def use_volcan_weapon(self):
        """Just not kill them"""
        return f'{self.bot_model} not have any weapon!'

    def launch_nuclear(self):
        """He can not this"""
        return f'{self.bot_model}, not have launcher!'

    def answer(self):
        """Hm..."""
        answer_1 = f'{self.bot_model} created to be your friend!'
        answer_2 = f'{self.bot_model} created to kill you.'
        answers = [answer_1, answer_2]
        return random.choice(answers)


sub_model_01 = SubKillBot('SXR-01', 'Little Killer', 'Stax')

print(sub_model_01.description())
print(f'Hm, he not kill... Kill count... {sub_model_01.victims}, nuclear kill '
      f'count... {sub_model_01.nuclear_victims}')
print(f'Ok, i just push this button... And... He, comes to live. '
      f'Good morning {sub_model_01.bot_model}. Do you want be human friend?')
print(sub_model_01.use_volcan_weapon())
print(sub_model_01.launch_nuclear())
print(f'Ah! WTF is that? Why do you exist? '
      f'{sub_model_01.bot_name}, answer me!')
print(sub_model_01.answer())
print(sub_model_01.os_system)
