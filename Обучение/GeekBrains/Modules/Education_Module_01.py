import os

# Моё исполнение функции создания папок:

list_of_dir = []


def make_dirs(num_dirs):
    for i in range(1, num_dirs + 1):
        list_of_dir.append('dir_' + str(i))

    for i in list_of_dir:
        os.mkdir(i)


def remove_dirs(num_dirs):
    for i in range(1, num_dirs + 1):
        list_of_dir.append('dir_' + str(i))

    for i in list_of_dir:
        os.rmdir(i)


# Иное исполнение функций создания или удаления папок: (Значительно лаконичней)

def another_make_dirs(num_dirs):
    for i in range(1, num_dirs + 1):
        directory_names = f'dir_{i}'
        os.mkdir(directory_names)


def another_remove_dirs(num_dirs):
    for i in range(1, num_dirs + 1):
        directory_names = f'dir_{i}'
        os.rmdir(directory_names)
