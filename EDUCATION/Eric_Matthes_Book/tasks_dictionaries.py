"""
Задачи из книги. --Глава 6. Словари
"""

print('Task 1\n')

# Любимые числа: используйте словарь для хранения любимых чисел.
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

# Глоссарий.
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

# Глоссарий 2.
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

# Страница 125
