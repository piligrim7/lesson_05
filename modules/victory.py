import random as rnd

def day_to_text(d):
    d_arr = d.split('.')
    num20 = ['первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого',
        'восьмого', 'девятого', 'десятого', 'одиннадцатого', 'двенадцатого',
        'тринадцатого', 'четырнадцатого', 'пятнадцатого', 'шестнадцатого',
        'семнадцатого', 'восемнадцатого', 'девятнадцатого', 'двадцатого']
    num2030 = ['двадцать', 'тридцать', 'тридцатого']
    month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    if int(d_arr[0]) < 21:
        dd=num20[int(d_arr[0]) - 1]
    elif d_arr[0] == '30':
        dd = num2030[2]
    else:
        dd = num2030[int(d_arr[0][0])-2] + ' ' + num20[int(d_arr[0][1]) - 1]
        
    mm = month[int(d_arr[1])-1]
    
    return dd, mm, d_arr[2]

def play_game():
    by = {
        'Пушкин':'06.06.1799',
        'Лермонтов':'15.10.1814',
        'Ломоносов':'19.11.1711',
        'Циолковский':'17.09.1857',
        'Путин':'07.10.1952',
        'Гайдай':'30.01.1923',
        'Никулин':'18.12.1921',
        'Гагарин':'09.03.1934',
        'Айвазовский':'29.07.1817',
        'Маяковский':'19.07.1893'
        }
    cnt_all = len(by) # Общее количество д/р знаменитостей в базе викторины
    cnt = 5 # Количество вопросов игроку
    repeat = True
    while repeat:
        ar = rnd.sample(range(cnt_all),cnt)
        correct = 0
        keys = list(by)
        for i in ar:
            g = input('Когда родился {}? (dd.mm.yyyy) '.format(keys[i]))
            result = g == by[keys[i]]
            if not result:
                dd,mm,yy = day_to_text(by[keys[i]])
                
                print('{} родился {} {} {} года'.format(keys[i], dd, mm, yy))
            correct += result
        print('Количество правильных ответов:', correct)
        print('Количество ошибок:', cnt - correct)
        repeat = input('Начать игру сначала (да/нет?) ') == 'да'