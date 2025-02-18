from zipfile import ZipFile
import os
import datetime

def make_reserve_arc(source, dest):
    # Проверка существования исходной и целевой директорий
    if not os.path.exists(source):
        print(f"Ошибка: Исходный каталог '{source}' не существует.")
        return
    if not os.path.exists(dest):
        print(f"Ошибка: Целевой каталог '{dest}' не существует.")
        return

    # Формирование имени архива с текущей датой и временем
    now = datetime.datetime.now()
    archive_name = now.strftime("%Y_%m_%d_%H_%M_%S") + ".zip"
    archive_path = os.path.join(dest, archive_name)

    # Создание архива
    with ZipFile(archive_path, 'w') as myzip:
        # Рекурсивный обход директории
        for foldername, subfolders, filenames in os.walk(source):
            # Добавляем пустые папки
            for subfolder in subfolders:
                full_folder_path = os.path.join(foldername, subfolder)
                arcname = os.path.relpath(full_folder_path, start=source)
                myzip.write(full_folder_path, arcname)
            
            # Добавляем файлы
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, start=source)
                myzip.write(file_path, arcname)

    print(f"Архив успешно создан: {archive_path}")

# Пример использования
make_reserve_arc(input('Введите путь к каталогу, который надо архивировать: '),
                 input('Введите путь к каталогу, в который необходимо поместить результат: '))
