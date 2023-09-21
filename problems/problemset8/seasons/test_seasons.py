import pytest 
from seasons import calculate_age
from datetime import date 

def test_today():
    assert calculate_age(date.fromisoformat('2023-09-20')) == 'Zero minutes'

def test_yesterday():
    assert calculate_age(date.fromisoformat('2023-09-19')) == 'One thousand, four hundred forty minutes'

def test_errorcheck():
    with pytest.raises(ValueError):
        calculate_age(date.fromisoformat('09-19-2023'))
        calculate_age(date.fromisoformat('09-19-23'))
        calculate_age(date.fromisoformat('09/18/2023'))
        calculate_age(date.fromisoformat('September 18, 2023'))
