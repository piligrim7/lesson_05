import os
from datetime import date
import modules.victory as victory
import modules.bank_bill as bbil
import modules.file_system_functions as fsf

def get_parameter(message: str)->str:
    return input(message)

if __name__ == '__main__':
    current_folder = os.getcwd()

    menu = {
        1:'создать папку',
        2:'удалить (файл/папку)',
        3:'копировать (файл/папку)',
        4:'просмотр содержимого рабочей директории',
        5:'сохранить содержимое рабочей директории',
        6:'посмотреть только папки',
        7:'посмотреть только файлы',
        8:'просмотр информации об операционной системе',
        9:'создатель программы',
        10:'играть в викторину',
        11:'мой банковский счет',
        12:'смена рабочей директории',
        13:'текущая дата',
        14:'выход'
    }

    while True:
        print('Меню:')
        [print(f'{n}. {item}') for n, item in menu.items()]
        s = input('Введите номер пункта меню: ')
        try:
            num = int(s)
        except:
            num = 0
        match num:
            case 1:
                path = current_folder + os.sep + get_parameter(
                    message='Введите имя создаваемой папки: '
                    )
                print(fsf.create_folder(path=path))
            case 2:
                path = current_folder + os.sep + get_parameter(
                    mes11sage='Введите имя удаляемой папки/файла: '
                    )
                print(fsf.delete_file_or_folder(path=path))

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
                print(fsf.save_dir_list(file_name='listdir.txt', path=current_folder))
            case 6:
                print(f'Папки в текущей директории {current_folder}:')
                print(fsf.get_dir_list_folders(path=current_folder))
            case 7:
                print(f'Файлы в текущей директории {current_folder}:')
                print(fsf.get_dir_list_files(path=current_folder))
            case 8:
                print(fsf.get_os_info())
            case 9:
                print(fsf.get_autor_name())
            case 10:
                victory.play_game()
            case 11:
                bbil.begin()
            case 12:
                path = get_parameter(
                    message='Введите путь к рабочей директории: '
                    )
                if fsf.check_folder(path=current_folder + os.sep + path):
                    current_folder = fsf.get_abs_path(current_folder + os.sep + path)
                    print(f'Рабочая директория изменена на {current_folder}')
                elif fsf.check_folder(path=path):
                    current_folder = fsf.get_abs_path(path)
                    print(f'Рабочая директория изменена на {current_folder}')
                else:
                    print(f'Указанная папка не найдена, рабочая директория не изменена!')
            case 13:
                print('Текущая дата:', date.today().strftime('%d %B %Y'))
            case 14:
                exit()
            case _:
                print(f'Указанный пункт меню не существует!')


