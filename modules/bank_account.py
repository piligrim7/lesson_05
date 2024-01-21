import os
import json

FILE_NAME = 'bank_account.json'

def add_order(bank_account: dict(), name: str, summ: float):
    result = bank_account.copy()
    result['summ']+=summ
    result['orders'].append(name)
    return result

def save_json(file_name:str, object: dict())->bool:
    try:
        with open(file_name, 'w') as f:
            json.dump(object, f)
        return True
    except:
        return False
    
def load_json(file_name:str):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            result = json.load(f)
    else:
        result = {'summ': 0.0, 'orders': []}   
    return result

def to_buy():
    bank_account = load_json(FILE_NAME)

    print('Программа "Мой банковский счет"')
    while True:
        print('Меню:')
        print('1. Добавить покупку')
        print('2. История покупок')
        print('3. Показать сумму расходов')
        print('4. Выход')
        choise = input('Введите номер пункта меню: ')
        if choise == '1':
            name = input('Введите название: ')
            while True:
                s = input('Введите сумму покупки: ')
                try:
                    summ = float(s)
                    bank_account = add_order(bank_account= bank_account, name=name, summ=summ)
                    break
                except:
                    print('Сумма введена некорректно')
        elif choise == '2':
            for order in bank_account['orders']:
                print(order)
        elif choise == '3':
            print(f'Сумма расходов {bank_account["summ"]}')
        elif choise == '4':
            save_json(FILE_NAME, bank_account)
            break
        else:
            print('Номер пункта меню выбран неверно')