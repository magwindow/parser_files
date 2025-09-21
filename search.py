import os
import shutil

KEY_FOR_SEARCH = input('Что ищем?\n')
PATH_FOR_COPY = input('Куда копировать файлы?\n')
FILES = input('Введите расширение файла: [.txt .png .mp3 и тд.]\n')


def search(select_files):
    """Функция - генератор, которая находит файлы в указанной директории"""
    for address, dirs, files in os.walk(input('Введите путь старта:\n')):

        # Пропускать файлы той директории, в которую идет копия
        if address == PATH_FOR_COPY:
            continue

        for file in files:
            if file.endswith(select_files):
                yield os.path.join(address, file)


def read_from_path_files(path):
    """Ищет указанный файл по названию и содержимому"""
    with open(path) as r:
        for e in r:
            if KEY_FOR_SEARCH in e:
                return copy(path)


def copy(path):
    """Копирует файлы в указанное место"""
    filename = path.split('\\')[-1]

    # Цикл проверяет если есть одинаковый файл с названием
    # то добавляет к нему цифру, например, license(1).txt, license(2).txt, license(3).txt
    count = 1
    while True:
        if os.path.isfile(os.path.join(PATH_FOR_COPY, filename)):
            if f'({count - 1})' in filename:
                filename = filename.replace(f'({count - 1})', '')
            filename = f'({count}).'.join(filename.split('.'))
            count += 1
        else:
            break

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, filename))
    print('Файл скопирован:', filename)


for i in search(FILES):
    try:
        read_from_path_files(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY, 'errors.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')
