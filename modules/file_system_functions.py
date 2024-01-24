import os
import platform
import shutil

def create_folder(path: str)->str:
    if not os.path.exists(path=path):
        try:
            os.mkdir(path=path)
            return f'Папка {path} создана.'
        except:
            return f'Ошбика при создании папки с именем {path}!'
    else:
        return f'Папка {path} уже существует!'
        
def delete_file_or_folder(path: str):
    if os.path.exists(path=path):
        try:
            os.rmdir(path=path)
            return f'Папка {path} удалена.'
        except:
            try:
                os.remove(path=path)
                return f'Файл {path} удален'
            except:
                return f'Ошибка при удалении папки/файла с именем {path}!'
    return f'Папка/файл {path} не существует!'

def copy_file_or_folder(path_source: str, path_dest: str):
    if path_dest==path_source:
        return f'Имя копируемой и новой папки/файла совпадают!'
    else:
        if os.path.exists(path=path_source):
            if os.path.exists(path=path_dest):
                return f'Папка/файл назначения {path_dest} уже существует!'
            else:
                try:
                    shutil.copy(src=path_source, dst=path_dest)
                    return f'Файл {path_source} скопирован в {path_dest}!'
                except:
                    try:
                        shutil.copytree(src=path_source, dst=path_dest,)
                        return f'Папка {path_source} скопирована в {path_dest}!'
                    except:
                        return f'Ошибка копирования Папки/файла {path_source} в {path_dest}!'
        else:
            return f'Копируемая папка/файл {path_source} не существует!'

def get_dir_list(path: str)->list[str]:
    return os.listdir(path=path) if os.path.isdir(path) else []

def get_dir_list_files(path: str)->list[str]:
    return [f for f in get_dir_list(path=path) if os.path.isfile(path+os.sep+f)]

def get_dir_list_folders(path: str)->list[str]:
    return [d for d in get_dir_list(path=path) if os.path.isdir(path+os.sep+d)]

def add_before_after(f)->str:
    def inner(some_list: list[str], before:str = '', after: str = '')->str:
        return before + f(some_list) + after
    return inner

@add_before_after
def list_to_str(some_list: list[str])->str:
    s=''
    for some in some_list:
        s += ', ' + some if s else some
    return s

def save_dir_list(file_name: str, path: str)->str:
    if os.path.exists(path=path):
        try:
            with open(file_name, 'w') as wf:
                f_list = get_dir_list_files(path=path)
                wf.write(list_to_str(some_list=f_list, before='files: ', after='\n'))
                dir_list = get_dir_list_folders(path=path)
                wf.write(list_to_str(some_list=dir_list, before='dirs: '))
            return f'Содержимое папки {path} сохранено в файл {file_name}.'
        except:
            return f'Ошибка сохранения в файл {file_name}!'
    else:
        return f'Папка {path} не существует!'

def get_os_info():
    return f'Информация о системе: {platform.platform()}'

def get_autor_name():
    return 'Создатель программы - Юрий Лысаков'

def get_bank_account():
    return 'Мой банковский счет - конфиденциальная информация'

def check_folder(path: str):
    return os.path.isdir(path)

def get_abs_path(path: str):
    return os.path.abspath(path=path)