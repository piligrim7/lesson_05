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
    if path_dest!=path_source:
        if os.path.exists(path=path_source):
            if not os.path.exists(path=path_dest):
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
                return f'Папка/файл назначения {path_dest} уже существует!'
        else:
            return f'Копируемая папка/файл {path_source} не существует!'
    else:
        return f'Имя копируемой и новой папки/файла совпадают!'

def get_dir_list(path: str)->list[str]:
    if os.path.isdir(path):
        return os.listdir(path=path)
    else:
        return []

def get_files_and_dirs(path: str)->([],[]):
    f_list = []
    dir_list = []
    l = get_dir_list(path=path)
    for f in l:
        if os.path.isdir(path+os.sep+f):
            dir_list.append(f)
        elif os.path.isfile(path+os.sep+f):
            f_list.append(f)
    return f_list, dir_list

def get_dir_list_folders(path: str)->list[str]:
    f_list, dir_list = get_files_and_dirs(path=path)
    return dir_list

def get_dir_list_files(path: str)->list[str]:
    f_list, dir_list = get_files_and_dirs(path=path)
    return f_list

def save_dir_list(file_name: str, path: str)->str:
    if os.path.exists(path=path):
        try:
            with open(file_name, 'w') as wf:
                f_list, dir_list = get_files_and_dirs(path=path)
                first = True
                s='files: '
                for f in f_list:
                    if first:
                        s += f
                        first = False
                    else:
                        s += ', ' + f
                wf.write(s+'\n')
                first = True
                s='dirs: '
                for f in dir_list:
                    if first:
                        s += f
                        first = False
                    else:
                        s += ', ' + f
                wf.write(s)
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