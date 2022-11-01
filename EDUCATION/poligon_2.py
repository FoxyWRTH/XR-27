"""
Полигон №2
"""
import json

PATH = 'elements.json'
with open(PATH, 'r', encoding='utf-8') as work_file:
    content = json.load(work_file)

print(content)
