import datetime
import os
import shutil


def create_new_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as work_file:
        if text:
            work_file.write(text)


def create_new_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует.')


# Функция На запрос списка содержимого директории. Если использовать параметр "True" Будет выведен список только папок.
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [i for i in result if os.path.isdir(i)]  # os.isdir() - проверка: является ли папкой.
    print(result)


def delete_file_or_folder(name):
    try:
        if os.path.isdir(name):  # Именно так выглядит проверка, является ли объект папкой!
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("Файл или папка не найдены.")
    except OSError:
        shutil.rmtree(name)


def copy_file_or_folder(name, direction):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, direction)
        else:
            shutil.copy(name, direction)
    except FileNotFoundError:
        print("Файл не найден.")
    except shutil.SameFileError:
        print("Такой файл/папка уже существуют.")


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as work_file:
        work_file.write(result + '\n')


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


# if __name__ == '__main__':
