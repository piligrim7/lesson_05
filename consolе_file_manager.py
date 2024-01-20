import os
import functions.file_system as fsf

def get_parameter(message: str)->str:
    return input(message)

current_folder = os.getcwd()

menu = {
    1:'создать папку',
    2:'удалить (файл/папку)',
    3:'копировать (файл/папку)',
    4:'просмотр содержимого рабочей директории',
    5:'посмотреть только папки',
    6:'посмотреть только файлы',
    7:'просмотр информации об операционной системе',
    8:'создатель программы',
    9:'играть в викторину',
    10:'мой банковский счет',
    11:'смена рабочей директории (*необязательный пункт)',
    12:'выход'
}

num = 0
while True:
    print('MENU:')
    for n, item in menu.items():
        print(f'{n}. {item}')
    num = int(input('Введите номер пункта меню: '))
    match num:
        case 1:
            path = current_folder + os.sep + get_parameter(
                message='Введите имя создаваемой папки: '
                )
            fsf.create_folder(path=path)
        case 2:
            path = current_folder + os.sep + get_parameter(
                message='Введите имя удаляемой папки/файла: '
                )
            fsf.delete_file_or_folder(path=path)

        case 3:
            path_source = current_folder + os.sep + get_parameter(
                message='Введите имя копируемой папки/файла: '
                )
            path_dest = current_folder + os.sep + get_parameter(
                message='Введите новое имя папки/файла: '
                )
            fsf.copy_file_or_folder(path_source=path_source, path_dest=path_dest)
        case 4:
            print(f'Содержимое текущей директории {current_folder}:')
            print(fsf.get_dir_list(path=current_folder))
        case 5:
            print(f'Папки в текущей директории {current_folder}:')
            print(fsf.get_dir_list_folders(path=current_folder))
        case 6:
            print(f'Файлы в текущей директории {current_folder}:')
            print(fsf.get_dir_list_files(path=current_folder))
        case 7:
            print('Информация о системе: ', fsf.get_os_info())
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            exit()
        case _:
            print(f'Пункт меню №{num} не существует!')


