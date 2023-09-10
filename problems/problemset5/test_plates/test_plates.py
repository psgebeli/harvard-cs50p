'''

INSTRUCTIONS
------------

In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still 
expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the 
value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py

'''

import plates

def test_rule1():

    assert plates.is_valid('A') == False
    assert plates.is_valid('AAAAAAAAA') == False
    assert plates.is_valid('AA11111') == False
    assert plates.is_valid('AAA') == True

def test_rule2():

    assert plates.is_valid('1111') == False
    assert plates.is_valid('A111') == False
    assert plates.is_valid('AAA1') == True 
    assert plates.is_valid('AA11') == True

def test_rule3():

    assert plates.is_valid('A11B') == False
    assert plates.is_valid('AB01') == False
    assert plates.is_valid('AB11CD') == False 
    assert plates.is_valid('AB10') == True

def test_rule4():

    assert plates.is_valid('ABCDE.') == False
    assert plates.is_valid('A!!3') == False 
    assert plates.is_valid('ABC?') == False 
    assert plates.is_valid('AA:;<>') == False



