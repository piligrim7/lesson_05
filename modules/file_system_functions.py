import os
import platform
import shutil

def create_folder(path: str):
    if not os.path.exists(path=path):
        os.mkdir(path=path)
        print(f'Папка {path} создана!')
    else:
        print(f'Папка {path} уже существует!')
        
def delete_file_or_folder(path: str):
    if os.path.exists(path=path):
        try:
            os.rmdir(path=path)
            print(f'Папка {path} удалена!')
        except:
            try:
                os.remove(path=path)
                print(f'Файл {path} удален!')
            except:
                print(f'Папка/файл {path} не существует!')

def copy_file_or_folder(path_source: str, path_dest: str):
    if path_dest!=path_source:
        if os.path.exists(path=path_source):
            if not os.path.exists(path=path_dest):
                try:
                    shutil.copy(src=path_source, dst=path_dest)
                    print(f'Файл {path_source} скопирован в {path_dest}!')
                except:
                    try:
                        shutil.copytree(src=path_source, dst=path_dest,)
                        print(f'Папка {path_source} скопирована в {path_dest}!')
                    except:
                        pass
            else:
                print(f'Папка/файл назначения {path_dest} уже существует!')
        else:
            print(f'Каопируемая папка/файл {path_source} не существует!')
    else:
        print(f'Имя копируемой и новой папки/файла совпадают!')

def get_dir_list(path: str)->list[str]:
    return os.listdir(path=path)

def get_dir_list_folders(path: str)->list[str]:
    result = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        result.extend(dirnames)
    return result

def get_dir_list_files(path: str)->list[str]:
    result = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        result.extend(filenames)
    return result

def get_os_info():
    return platform.platform()

def check_folder(path: str):
    return os.path.isdir(path)

def get_abs_path(path: str):
    return os.path.abspath(path=path)