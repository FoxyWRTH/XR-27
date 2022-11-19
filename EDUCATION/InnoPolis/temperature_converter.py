"""
17.11 лекция.
"""


def temperature_converter():
    """
    Собирает информацию для конвертера.
    :return: температуру и тип.
    """
    try:
        temper = float(input('Введите температуру в цельсиях,'
                             ' используйте только цифровые значения.\n'
                             'Пример: 23 | 123,3 | 36,6\n'))
    except ValueError:
        return print(
            'Для указания температуры используйте цифровое значение.')
    chose_convert = input('В какой формат нужно конвертировать цельсии?\n'
                          'Пример: фаренгейт | Кельвин | far | kel\n')
    if chose_convert.lower() in ('фаренгейт', 'far'):
        result_f = (float(temper) * 1.8) + 32
        return f'Температура по Фаренгейту: {round(result_f, 2)}°F'
    if chose_convert.lower() in ('кельвин', 'kel'):
        result_k = (float(temper)) + 273.15
        return f'Температура по Кельвину: {round(result_k, 2)}°K'
    return 'Укажите в цифровом формате температуру в цельсиях,' \
           ' а так же тип для конвертации.'


print(temperature_converter())
