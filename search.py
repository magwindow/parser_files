import os
import shutil

KEY_FOR_SEARCH = input('Что ищем?\n')
FILES = input('Введите расширение файла: [.txt .png .mp3 и тд.]\n')


def search(select_files):
    """Функция - генератор, которая находит файлы в указанной директории"""
    for address, dirs, files in os.walk(input('Введите путь старта:\n')):
        for file in files:
            if file.endswith(select_files):
                yield os.path.join(address, file)


def read_from_path_files(path):
    """Ищет указанный файл по названию и содержимому"""
    with open(path, 'r', encoding='utf-8') as r:
        for e in r:
            if KEY_FOR_SEARCH in e:
                return path


for i in search(FILES):
    try:
        print(read_from_path_files(i))
    except Exception as e:
        with open('errors.txt', 'a', encoding='utf-8') as r:
            r.write(str(e) + '\n' + i + '\n')
