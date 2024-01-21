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

