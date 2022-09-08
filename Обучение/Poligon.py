a = 881
b = 0
c = 2

try:
    print(a / b)
except:
    print('No')

try:
    player_range_count = input('Введите диапазон чисел. \n')
    player_try_count = input('Введите желаемое количество попыток. \n')
except ValueError:
    print('No')
    exit()