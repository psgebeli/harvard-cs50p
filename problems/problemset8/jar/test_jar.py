import pytest 
from jar import Jar

def test_withdraw():

    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(3)
        jar.withdraw(1)
   # assert jar.withdraw(0) == 0 

def test_deposit():


    for i in range(1, 11):
        jar = Jar(capacity=10)
        assert jar.deposit(i) == i 
    with pytest.raises(ValueError):
        jar.deposit(11)
        jar.deposit(-1)
    
def test_str():

    jar = Jar()
    jar.deposit(3)
    assert jar.__str__() ==  '🍪🍪🍪'
    jar.deposit(2)
    assert jar.__str__() == '🍪🍪🍪🍪🍪'


