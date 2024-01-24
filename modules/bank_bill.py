import os
import json

FILE_NAME = 'bank_bill.json'

def add_product(bill: dict(), name: str, cost: float):
    bill = bill.copy()
    bill['bill']-=cost
    bill['products'].append([name, cost])
    return bill

def save_json(file_name:str, bill: dict())->bool:
    try:
        with open(file_name, 'w') as f:
            json.dump(bill, f)
        return True
    except:
        return False
    
def load_json(file_name:str):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            result = json.load(f)
    else:
        result = {'bill': 0.0, 'products': []}   
    return result

def begin():
    bill: dict() = load_json(FILE_NAME)

    print('Программа "Личный счет"')
    while True:
        print('Меню:')
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        choise = input('Введите номер пункта меню: ')
        if choise == '1':
            s = input('Введите сумму пополнения счета: ')
            try:
                summ = float(s)
                bill['bill'] += summ
                print('Сумма на счету:', bill['bill'])
            except:
                print('Сумма введена некорректно')
        elif choise == '2':
            s = input('Введите стоимость товара: ')
            try:
                cost = float(s)
                if cost<bill['bill']:
                    name = input('Введите название товара: ')
                    bill = add_product(bill=bill, name=name, cost=cost)
            except:
                print('Сумма введена некорректно')
        elif choise == '3':
            for name, cost in bill['products']:
                print(f'Товар: {name}, стоимость {cost}')
        elif choise == '4':
            save_json(FILE_NAME, bill)
            break
        else:
            print('Номер пункта меню выбран неверно')