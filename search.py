import os
import shutil

FILES = input('Введите расширение файла: [.txt .png .mp3 и тд.]\n')


def search(select_files):
    for address, dirs, files in os.walk(input('Введите путь старта:\n')):
        for file in files:
            if file.endswith(select_files):
                yield os.path.join(address, file)


for i in search(FILES):
    print(i)
