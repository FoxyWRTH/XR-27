"""
Заметки из книги
"""

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
