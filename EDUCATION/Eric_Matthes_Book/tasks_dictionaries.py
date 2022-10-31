"""
Задачи из книги. --Глава 6. Словари
"""

print('Task 1\n')

# Любимые числа: (6.2)
# используйте словарь для хранения любимых чисел.
# Возьмите пять имен и используйте их как ключи словаря.
# Придумайте любимое число для каждого человека
# И сохраните его как значение в словаре.
# Выведите имя каждого человека и его любимое число.

dictionaries_of_numbers = {
    'Alex': '5',
    'Greta': '69',
    'Alisa': '32',
    'Mark': '22',
    'Gordon': '3'
}

print(dictionaries_of_numbers)

print('\nTask 2\n')

# Глоссарий. (6.3)
# Словари Python могут использоваться для моделирования «настоящего» словаря
# (чтобы не создавать путаницу, назовем его глоссарием):
# Вспомните пять лисьих ключей.
# Используйте эти слова как ключи глоссария, а их определения — как значения.
# Выведите каждое слово и его определение в аккуратно отформатированном виде.

fox_keys = {
    '1': 'Одна лиса расскажет тебе "сказку"...',
    '2': 'Две лисы повергнут тебя в "отчаяние"...',
    '3': 'Три лисы помогут "советом"...',
    '4': 'Четыре лисы тебя не "знают"',
    '5': 'Пять лис могут вывести тебя к "свету"...'
}

print(f'У Лиса есть 5 ключей.\n'
      f'Первый: {fox_keys.get("1")}\n'
      f'Второй: {fox_keys.get("2")}\n'
      f'Третий: {fox_keys.get("3")}\n'
      f'Четвёртый: {fox_keys.get("4")}\n'
      f'Пятый: {fox_keys.get("5")}')

print('\nTask 3\n')

# Глоссарий 2. (6.4)
# Теперь, когда вы знаете, как перебрать элементы словаря,
# упростите код из упражнения 2, заменив серию команд print циклом.

for key, value in fox_keys.items():
    print(f'Ключ № {key}: {value}')

print('\nTask 3 Заметка.\n')

# Примечание: Вложение в словарь списков и перебор.

fox_keys_advanced = {
    '1': ['Одна лиса расскажет тебе "сказку"...', 'сказка'],
    '2': ['Две лисы повергнут тебя в "отчаяние"...', 'отчаяние'],
    '3': ['Три лисы помогут "советом"...', 'совет'],
    '4': ['Четыре лисы тебя не "знают"', 'знание'],
    '5': ['Пять лис могут вывести тебя к "свету"...', 'свет']
}

for key, value in fox_keys_advanced.items():
    print(f'Ключ № {key}, {value[0]} --ответ: {value[1]}')

print('\nTask 4\n')

# Люди. (6.7)
# Создайте два новых словаря, представляющих разных людей
# и сохраните все три словаря в списке с именем people.
# Переберите элементы списка людей.
# В процессе перебора выведите всю имеющуюся информацию о каждом человеке.

human_1 = {
    'first_name': 'alex',
    'last_name': 'gordon',
    'age': '31',
    'city': 'orlean'
}

human_2 = {
    'first_name': 'mark',
    'last_name': 'gordon',
    'age': '30',
    'city': 'toronto'
}

human_3 = {
    'first_name': 'alice',
    'last_name': 'freeman',
    'age': '31',
    'city': 'berlin'
}

people = [human_1, human_2, human_3]

for number, info in enumerate(people):
    print(f'Person №-{number + 1}\n'
          f'-Name: {info["first_name"].title()}\n'
          f'-Family: {info["last_name"].title()}\n'
          f'-Age: {info["age"].title()}\n'
          f'-City: {info["city"].title()}')

print('\nTask 5\n')

# Домашние животные (6.8)
# создайте несколько словарей
# имена которых представляют клички домашних животных.
# В каждом словаре сохраните информацию о виде животного и имени владельца.
# Сохраните словари в списке с именем pets.
# Переберите элементы списка.
# В процессе перебора выведите всю имеющуюся информацию о каждом животном.

mia = {
    'view': 'cat',
    'owner': 'lexy'
}
pickle = {
    'view': 'rat',
    'owner': 'mark'
}
hitler = {
    'view': 'dog',
    'owner': 'alice'
}

pets = [mia, pickle, hitler]

for number, info in enumerate(pets):
    print(f'Pet №-{number + 1}\n'
          f'-Owner name: {info["owner"].title()}\n'
          f'-Pet view: {info["view"].title()}')

print('\nTask 6\n')

# Любимые места -- Я так и не понял до конца, что от меня хотели. (6.9)
# Создайте словарь с именем favorite_places.
# Придумайте названия трех мест, которые станут ключами словаря
# и сохраните для каждого человека от одного до трех любимых мест.
# Переберите данные в словаре
# выведите имя каждого человека и его любимые места.

favorite_places = {
    'river': {
        'alex': ['river', 'bridge', 'cliff']
    },
    'bridge': {
        'alice': ['bringe', 'river']
    },
    'cliff': {
        'mark': ['bridge', 'cliff']
    }
}

for key, value in favorite_places.items():
    for name, place in value.items():
        print(f'Name: {name.title()}')
        for i in place:
            print(f'Favorite place: -{i.title()}')

print('\nTask 7\n')

# Любимые числа. (6.10)
# Измените программу из упражнения. (6.2)
# Чтобы для каждого человека можно было хранить более одного любимого числа.
# Выведите имя каждого человека в списке и его любимые числа.

dictionaries_of_numbers = {
    'Alex': {
        'number_1': '5',
        'number_2': '12',
        'number_3': '22'
    },
    'Greta': {
        'number_1': '1',
        'number_2': '323',
        'number_3': '54'
    },
    'Alisa': {
        'number_1': '34',
        'number_2': '24',
        'number_3': '52'
    },
    'Mark': {
        'number_1': '121',
        'number_2': '65',
        'number_3': '84'
    },
    'Gordon': {
        'number_1': '87',
        'number_2': '552',
        'number_3': '911'
    }
}

for name, value in dictionaries_of_numbers.items():
    print(f'Name: {name}')
    for info in value.values():
        print(f'Favorite number: {info}')

print('\nTask 8\n')

# Города. (6.11)
# Создайте словарь с именем cities.
# Используйте названия трех городов в качестве ключей словаря.
# Создайте словарь с информацией о каждом городе.
# Включите в него страну, в которой расположен город
# примерную численность населения и один примечательный
# факт, относящийся к этому городу.
# Ключи словаря каждого города должны называться:
# country, population и fact.
# Выведите название каждого города и всю сохраненную информацию о нем.

cities = {
    'orenburg': {
        'country': 'russia',
        'population': '572.308',
        'fact': 'Little city... My homeland'
    },
    'moscow': {
        'country': 'russia',
        'population': '10.382.754',
        'fact': 'One of the first places where nuclear missiles will fly.'
    },
    'omsk': {
        'country': 'russia',
        'population': '1.372.900',
        'fact': 'Where is that?'
    }
}

for key, value in cities.items():
    print(f'Name of city: {key.title()}')
    for key_2, value_2 in value.items():
        print(f'{key_2.title()}: {value_2.capitalize()}')

# Заполнение словарями списка с помощью цикла.
# Присвоение разных значений к элементам словаря циклом.

alien_swarm = []

for yellow_alien in range(5):  # Заполнение списка словарями.
    black_alien = {'color': 'black',
                   'health': '50',
                   'points': '10'}
    alien_swarm.append(black_alien)

for yellow_alien in range(5):  # Заполнение списка словарями.
    pink_alien = {'color': 'pink',
                  'health': '10',
                  'points': '75'}
    alien_swarm.append(pink_alien)

print(alien_swarm, f'\nTotal: {len(alien_swarm)}')

for yellow_alien in alien_swarm[0:3]:  # Присвоение иных значений элементам.
    if yellow_alien['color'] == 'black':  # Условие замены: совпадение ключа.
        yellow_alien['color'] = 'yellow'
        yellow_alien['health'] = '75'
        yellow_alien['points'] = '25'

for red_alien in alien_swarm[3:7]:  # Присвоение иных значений элементам.
    if red_alien['color'] == 'pink':  # Условие замены: совпадение ключа.
        red_alien['color'] = 'red'
        red_alien['health'] = '100'
        red_alien['points'] = '50'

print(alien_swarm)
