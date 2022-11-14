"""
Домашняя работа. Лекция №6
"""

from collections import Counter
import re

# Task - 1/2
# 1. Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# получить список кортежей
# (<remote_addr>, <request_type>, <requested_resource>)
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов.

# Заметки: Что бы возвращать цельное значение в кортеже используй ("str",)
path_to_file = ''
ip = []
with open(path_to_file, 'r', encoding='utf-8') as work_file:
    for line in work_file:
        separator = '"| - - | '
        remote_addr = (re.split(separator, line)[0],)
        request_type = (re.split(separator, line)[4],)
        requested_resource = (re.split(separator, line)[5],)
        print(f'{remote_addr}'
              f'{request_type}'
              f'{requested_resource}'
              .replace(',', ''))
        ip.append(remote_addr)

# С помощью "Counter" уточняю максимальное количество запросов.
max_count_of_request = max(Counter(ip).values())


def get_spam_id(request_count):
    """
    :param request_count: Передаём максимальное значение запросов.
    :return ИД с наибольшим количеством запросов.
    """
    for key, value in Counter(ip).items():
        if request_count == value:
            return key


print(f'User with ID {get_spam_id(max_count_of_request)} '
      f'made the most requests: {max_count_of_request}'.replace(',', ''))
