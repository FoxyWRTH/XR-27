"""
Полигон №1
"""
import json

list_of_elements_01 = ['M3', 'L2', 'D8', 'X1']

FILE_NAME = 'elements.json'

with open(FILE_NAME, 'w', encoding='utf-8') as work_file:
    json.dump(list_of_elements_01, work_file)
