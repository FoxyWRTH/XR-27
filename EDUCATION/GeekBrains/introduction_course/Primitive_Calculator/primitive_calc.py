while True:
    param_a = int(input())
    param_b = int(input())
    param_c = str(input())
    if param_c == '+':
        print(f'{param_a} + {param_b} =', param_a + param_b)
    elif param_c == '-':
        print(f'{param_a} - {param_b} =', param_a - param_b)
    elif param_c == '*':
        print(f'{param_a} * {param_b} =', param_a * param_b)
    elif param_c == '/' and param_b != 0:
        print(f'{param_a} / {param_b} =', param_a / param_b)
    elif param_c == '/' and param_b == 0:
        print('На ноль делить нельзя!')
    else:
        print('Неверная операция')
