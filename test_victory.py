import modules.victory as victory

def test_day_to_text():
    assert victory.day_to_text('07.08.1926')==('седьмого', 'августа', '1926')
    assert victory.day_to_text('31.12.2023')==('тридцать первого', 'декабря', '2023')