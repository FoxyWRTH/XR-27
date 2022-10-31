"""
Задачи из книги. --Глава 10. Файлы
"""

# Гость. (10.3, 10.4, 10.5)
# Напишите программу, которая запрашивает у пользователя его имя.
# Введенный ответ сохраняется в файле с именем guest.txt

PERSON_DATA = 'Hello and welcome! Please enter you answers on my questions.'
NAME = ''
AGE = ''
LOCATION = ''
CAUSES = []

while True:
    if NAME == '':
        NAME = input('What is your name?\n')
    if AGE == '':
        AGE = input('How old are you? Please use only digits\n')
    if LOCATION == '':
        LOCATION = input('Where you from?\n')
    if len(CAUSES) == 0:
        for i in range(1, 3 + 1):
            if i == 1:
                temp = input(f'What is your causes to work programmer?\n'
                             f'Enter cause №{i}\n')
                CAUSES.append(temp)
            else:
                temp = input(f'Enter cause №{i}\n')
                CAUSES.append(temp)
    if NAME != '' and AGE != '' and LOCATION != '' and len(CAUSES) != 0:
        break

print('Thank you! We save this information for your profile.')

PATH = 'education_files/education_some_info.txt'

with open(PATH, 'w', encoding='utf-8') as work_file:
    work_file.write(f'Well, what we got here...\n'
                    f'Name: {NAME}\n'
                    f'Age: {AGE}\n'
                    f'Location: {LOCATION}\n'
                    f'Causes...\n'
                    f'1: {CAUSES[0]}\n'
                    f'2: {CAUSES[1]}\n'
                    f'3: {CAUSES[2]}\n'
                    f'I hope he can...')
