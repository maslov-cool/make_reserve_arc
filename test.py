from zipfile import ZipFile
import os
import datetime


def make_reserve_arc(source, dest):
    archive_path = os.path.join(dest,
                                f'{str(datetime.datetime.now()).split('.')[0].replace(' ', '_').
                                   replace('-', '_').replace(':', '_')}.zip')
    with ZipFile(archive_path, 'w') as myzip:
        base_folder_name = os.path.basename(source)
        for currentdir, dirs, files in os.walk(source):
            for i in files:
                try:
                    myzip.write(os.path.abspath(i)[os.path.abspath(i).index(base_folder_name):])
                except FileNotFoundError:
                    pass
            folders = dirs.copy()
            while folders:
                for el in folders:
                    for currentdir1, dirs1, files1 in os.walk(el):
                        for i in files1:
                            try:
                                myzip.write(os.path.abspath(i)[os.path.abspath(i).index(base_folder_name):])
                            except FileNotFoundError:
                                pass
                        folders += dirs1
                    del folders[folders.index(el)]


make_reserve_arc(input('путь к каталогу, который надо архивировать '),
                 input('путь к каталогу, в который необходимо поместить результат '))