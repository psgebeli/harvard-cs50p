import pytest
from working import convert


def test_convert_success():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:00 PM to 5:00 AM') == '21:00 to 05:00'
    assert convert('12:00 AM to 8:00 AM') == '00:00 to 08:00'
    assert convert('5:41 AM to 1:47 PM') == '05:41 to 13:47'

def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_values():
    with pytest.raises(ValueError):
        convert('8:81 AM to 5:45 PM')
        convert('16 PM to 24 PM')


        