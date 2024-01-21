import os
import modules.bank_account as ba

bank_account = {'summ': 22.22,
                'orders': ['order1', 'order2', 'order3', 'order4']}

def test_add_order():
    assert ba.add_order(
        bank_account=bank_account,
        name='order5',
        summ=11.11
        )['orders'][4] == 'order5'
    assert ba.add_order(
        bank_account=bank_account,
        name='order5',
        summ=11.11
        )['summ'] == 33.33

def test_save_json():
    file_name = '?'
    assert ba.save_json(file_name=file_name, object=bank_account)==False
    file_name = 'q/q'
    assert ba.save_json(file_name=file_name, object=bank_account)==False
    file_name = 'test.json'
    assert ba.save_json(file_name=file_name, object=bank_account)
    assert os.path.isfile(path=file_name)
    os.remove(file_name)

def test_load_json():
    file_name = '?'
    assert ba.load_json(file_name=file_name) == {'summ': 0.0, 'orders': []}
    file_name = 'q/q'
    assert ba.load_json(file_name=file_name) == {'summ': 0.0, 'orders': []}
    file_name = 'test.json'
    assert ba.load_json(file_name=file_name)=={'summ': 0.0, 'orders': []}
    ba.save_json(file_name=file_name, object=bank_account)
    assert ba.load_json(file_name=file_name)==bank_account
    os.remove(file_name)
