import os
import modules.file_system_functions as fsf

def test_get_autor_name():
    assert fsf.get_autor_name() == 'Создатель программы - Юрий Лысаков'

def test_get_bank_account():
    assert fsf.get_bank_account() == 'Мой банковский счет - конфиденциальная информация'

def test_create_folder():
    path = 'some_folder_name_9876501234'
    assert fsf.create_folder(path=path)==f'Папка {path} создана.'
    assert fsf.create_folder(path=path)==f'Папка {path} уже существует!'
    os.rmdir(path=path)
    path = 'some_folder_name?_9876501234'
    assert fsf.create_folder(path=path)==f'Ошбика при создании папки с именем {path}!'
    path = 'some_folder_name\_9876501234'
    assert fsf.create_folder(path=path)==f'Ошбика при создании папки с именем {path}!'

def test_delete_file_or_folder():
    path = 'some_folder_name_9876501234'
    assert fsf.delete_file_or_folder(path=path)==f'Папка/файл {path} не существует!'
    os.mkdir(path=path)
    assert fsf.delete_file_or_folder(path=path)==f'Папка {path} удалена.' and not os.path.exists(path=path)
    if os.path.isdir(path):
        os.rmdir(path=path)
    path = 'some_folder_name_9876501234.txt'
    assert fsf.delete_file_or_folder(path=path)==f'Папка/файл {path} не существует!'
    f = open(path, 'w')
    f.close()
    assert fsf.delete_file_or_folder(path=path)==f'Файл {path} удален' and not os.path.exists(path=path)
    if os.path.isfile(path):
        os.remove(path=path)

def test_copy_file_or_folder():
    path_source = '?'
    path_dest = '?'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Имя копируемой и новой папки/файла совпадают!'
    path_source = ','
    path_dest = '?'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Копируемая папка/файл {path_source} не существует!'
    path_source = 'some_folder_name_9876501234'
    os.mkdir(path=path_source)
    path_dest = '?'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Ошибка копирования Папки/файла {path_source} в {path_dest}!'
    path_dest = 'some_folder_name_9876501234_1'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Папка {path_source} скопирована в {path_dest}!'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Папка/файл назначения {path_dest} уже существует!'
    os.rmdir(path=path_source)
    os.rmdir(path=path_dest)
    
    path_source = 'some_file_name_9876501234.txt'
    f = open(path_source, 'w')
    f.close()
    path_dest = 'some_file_name_9876501234_1.txt'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Файл {path_source} скопирован в {path_dest}!'
    assert fsf.copy_file_or_folder(
        path_source = path_source,
        path_dest = path_dest
        )==f'Папка/файл назначения {path_dest} уже существует!'
    os.remove(path=path_source)
    os.remove(path=path_dest)

def test_save_dir_list():
    file_name = 'some_file_name_9876501234.txt'
    path = 'some_folder_name_9876501234'
    assert fsf.save_dir_list(file_name=file_name,
                             path=path)==f'Папка {path} не существует!'
    os.mkdir(path=path)
    assert fsf.save_dir_list(file_name=file_name,
                             path=path)==f'Содержимое папки {path} сохранено в файл {file_name}.'
    os.remove(file_name)
    os.rmdir(path=path)

def test_list_to_str():
    some_list:list[str] = [str(i) for i in range(10)]
    assert fsf.list_to_str(some_list=some_list) == '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'