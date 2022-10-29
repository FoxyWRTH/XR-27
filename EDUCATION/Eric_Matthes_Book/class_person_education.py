"""
Класс для интеграции. И наследования.
"""


class Person():
    """Человек"""

    def __init__(self, name, age):
        """Инициализация атрибутов родительского класса"""
        self.name = name
        self.age = age

    def greetings(self):
        """Родительский метод приветствия"""
        return print(f'Hello {self.name}! Nice to see you!')

    def person_info(self):
        """Родительский метод получения информации из атрибутов"""
        return print(f'Person Name: {self.name}\n'
                     f'Person Age: {self.age}')


class ProfessionType(Person):
    """Класс профессии"""

    def __init__(self, name, age, profession, exp):
        """Инициализация атрибутов"""
        # Person.__init__(self, name, age)  # Выполняется унаследование.
        super().__init__(name, age)  # Более предпочтительный способ.
        self.profession = profession
        self.exp = exp

    def profession_type(self):
        """Метод вызова информации из атрибута |profession|"""
        return print(f'Person profession: {self.profession}')

    def experience(self):
        """Метод вызова информации из атрибута |exp|"""
        return print(f'Person experience: {self.exp}')


class Animal():  # pylint: disable=too-few-public-methods
    """Создание класса"""

    def __init__(self, name):
        """Инициализация атрибутов"""
        self.name = name

    def eat(self):
        """Животное ест"""
        print(f'{self.name} is eating.')


class Dog(Animal):
    """Класс Собака"""

    def __init__(self, name, breed):
        """Инициализация атрибутов класса"""
        super().__init__(name)
        self.breed = breed

    def bark(self):
        """Собака лает"""
        print(f'Dog named {self.name} is barking')

    def dog_breed(self):
        """Порода собаки"""
        print(f'This dog is {self.breed} breed!')


class Cat(Animal):
    """Класс Кошка"""

    def meow(self):
        """Кошка мяукает"""
        print(f'{self.name} says Meow!')


class Frog(Animal):  # pylint: disable=too-few-public-methods
    """Класс Лягушка"""

    def eat(self):
        """Лягушка ест (Переопределение родительского метода"""
        print(f'Frog with name {self.name} is eating!')


if __name__ == '__main__':
    unit_01 = ProfessionType('Foxy', 31, 'Programmer', 1)

    print()
    print(
        f'Hello and welcome {unit_01.name}, i see you {unit_01.age} year old '
        f'and also i see you are {unit_01.profession} with '
        f'{unit_01.exp} years experience')
    print()

    dog = Dog('Sharik', 'Sheepdog')
    cat = Cat('Mia')
    frog = Frog('Mr. Frog')

    dog.eat()
    dog.bark()
    dog.dog_breed()
    print()

    cat.eat()
    cat.meow()
    print()

    frog.eat()
