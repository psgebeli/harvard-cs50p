import pytest 
from numb3rs import validate

def testnum_range():
    assert validate('0.1.2.3')
    assert validate('255.2.3.4')
    assert not validate('256.2.3.4')
    assert not validate('300.2.3.4')
    assert validate('1.0.2.3')
    assert validate('1.255.2.3')
    assert not validate('1.256.2.3')
    assert not validate('1.300.2.3')
    assert validate('1.2.0.3')
    assert validate('1.2.255.3')
    assert not validate('1.2.256.3')
    assert not validate('1.2.300.3')
    assert validate('1.2.3.0')
    assert validate('1.2.3.255')
    assert not validate('1.2.3.256')
    assert not validate('1.2.3.300')

def test_nonnumeric():
    assert not validate('#.3.4.5')
    assert not validate('1.!.3.4')
    assert not validate('1.2..3.4')
    assert not validate('1.2.3.$')



