import os
import modules.bank_bill as bbil

bill = {'bill': 44.44,
                'products': [['product1', 2],['product2', 4],['product3', 6],['product4',8]]}

def test_add_product():
    assert bbil.add_product(
        bill=bill,
        name='product5',
        cost=11.11
        )['products'][4] == ['product5', 11.11]
    assert bbil.add_product(
        bill=bill,
        name='product5',
        cost=11.11
        )['bill'] == 33.33

def test_save_json():
    file_name = '?'
    assert bbil.save_json(file_name=file_name, bill=bill)==False
    file_name = 'q/q'
    assert bbil.save_json(file_name=file_name, bill=bill)==False
    file_name = 'test.json'
    assert bbil.save_json(file_name=file_name, bill=bill)
    assert os.path.isfile(path=file_name)
    os.remove(file_name)

def test_load_json():
    file_name = '?'
    assert bbil.load_json(file_name=file_name) == {'bill': 0.0, 'products': []}
    file_name = 'q/q'
    assert bbil.load_json(file_name=file_name) == {'bill': 0.0, 'products': []}
    file_name = 'test.json'
    assert bbil.load_json(file_name=file_name)=={'bill': 0.0, 'products': []}
    bbil.save_json(file_name=file_name, bill=bill)
    assert bbil.load_json(file_name=file_name)==bill
    os.remove(file_name)