"""
Домашняя работа. Лекция №4
"""

import re
import datetime
import requests

# Task - 2/3

# Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
# отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp
# *
# Доработать функцию currency_rates(): теперь она должна возвращать кроме
# курса дату, которая передаётся в ответе сервера. Дата должна быть в виде
# объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?

URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
answer = requests.get(URL, timeout=10).text

finding = re.split('>|<|</|/', answer)  # Распиливаю общую массу информации.

finding_date = finding[3].split('"')[1].split('.')  # Изолирую дату.

date = datetime.date(int(finding_date[2]),  # Помещаю части даты
                     int(finding_date[1]),  # В нужные отсеки.
                     int(finding_date[0]))


def current_rates(money_code):
    """
    :param money_code: литерал валюты
    :return Форматированный ответ сайта в удобоваримом виде.
    """
    if money_code.upper() in finding:  # Убираю зависимость регистра.
        index = finding.index(money_code.upper())  # Нахождение индекса валюты.
        name_money = finding[index + 10]  # Нахождение название валюты.
        value_money = finding[index + 5]  # Нахождение количество валюты.
        code_money = finding[index]  # Аббревиатура валюты.
        russian_rub = finding[index + 15].replace(',', '.')  # Сумма в рублях.
        result = f'Вы выбрали: "{name_money}"\n{value_money} единица "' \
                 f'{code_money}" = {float(russian_rub)} "RUB"\n' \
                 f'Дата запроса: {date}'
        return result
    return None


if __name__ == '__main__':
    print(current_rates('eur'))
