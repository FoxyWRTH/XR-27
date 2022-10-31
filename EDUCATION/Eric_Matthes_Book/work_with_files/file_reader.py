"""
Задачи из книги. --Глава 10. Файлы (Чтение файла, запись, добавление)
"""

PATH = 'C:/Users/FXR-34/Desktop/Алиса в стране чудес .txt'

with open(PATH, 'r', encoding='windows-1251') as work_file:
    content = work_file.read()
    words = content.split()

print(words)
print(len(words))
