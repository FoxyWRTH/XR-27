"""
Основной каркас тестового файлового менеджера.
"""
import sys
import os
from colorama import Fore, Style
from core import create_new_folder, create_new_file, copy_file_or_folder, \
    delete_file_or_folder, get_list

FAILURE_MESSAGE = 'Не задан параметр'

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду.')
else:
    if command == 'list':
        try:
            FLAG = sys.argv[2]
            get_list(FLAG)
        except IndexError:
            get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print(FAILURE_MESSAGE)
        else:
            create_new_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print(FAILURE_MESSAGE)
        else:
            create_new_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print(FAILURE_MESSAGE)
        else:
            delete_file_or_folder(name)
    elif command == 'copy_file_or_folder':
        try:
            name = sys.argv[2]
            direction = sys.argv[3]
        except IndexError:
            print(FAILURE_MESSAGE)
        else:
            copy_file_or_folder(name, direction)
    elif command == 'work_dir':
        print(Fore.RED + 'Current Work Directory: ' + Fore.BLUE
              + os.getcwd() + Style.RESET_ALL)
    elif command == 'help':
        print(Fore.RED + '"list"' + Fore.GREEN +
              ' Запросить список файлов и папок')
        print(Fore.RED + '"create_file"' + Fore.GREEN +
              ' Создать файл, укажите через пробел название файла')
        print(Fore.RED + '"create_folder"' + Fore.GREEN +
              ' Создать папку, укажите через пробел название папки')
        print(Fore.RED + '"delete"' + Fore.GREEN +
              ' Удаление файла или папки')
        print(Fore.RED + '"copy_file_or_folder"' + Fore.GREEN +
              ' Копирование файлов и папок' + Style.RESET_ALL)
        print(Fore.RED + '"work_dir"' + Fore.GREEN +
              ' Рабочая директория')
