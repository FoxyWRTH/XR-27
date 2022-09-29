"""
Домашняя работа. Лекция №4
"""

import re
import requests

URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
answer = requests.get(URL, timeout=10).text

finding = re.split('>|<|</|/', answer)


def current_rates(money_code):
    """
    :param money_code: литерал валюты
    :return собранные куски ответа сайта в удобоваримом виде.
    """
    if money_code.upper() in finding:
        index = finding.index(money_code.upper())  # Нахождение индекса валюты.
        name_money = finding[index + 10]  # Название валюты.
        value_money = finding[index + 5]  # Количество валюты.
        code_money = finding[index]  # Аббревиатура валюты.
        russian_rub = finding[index + 15].replace(',', '.')  # Сумма в рублях.
        result_date = finding[3].split('"')[1]  # Дата.
        result = f'Вы выбрали: "{name_money}"\n{value_money} единица "' \
                 f'{code_money}" = {float(russian_rub)} "RUB"\n' \
                 f'Дата запроса: {result_date}'
        return result
    return None


if __name__ == '__main__':
    print(current_rates('cny'))
