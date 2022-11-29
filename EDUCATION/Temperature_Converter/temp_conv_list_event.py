"""
Случайные события.
"""
import random
import time


def rnd_wrong_answer():
    """Случайное шутливое событие"""
    generate_num = 0
    rnd = random.SystemRandom()

    print('Получаю доступ к твоей системе.')

    while True:
        mem_num = generate_num
        generate_num = rnd.randint(generate_num, generate_num + 33)
        time.sleep(rnd.uniform(0.2, 1.5))
        if generate_num >= 100:
            print('...100%')
            break
        if generate_num != mem_num:
            print(f'...{generate_num}%')

    print('Доступ получен.')


if __name__ == '__main__':
    rnd_wrong_answer()
