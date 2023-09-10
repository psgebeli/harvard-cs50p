'''

INSTRUCTIONS
------------

In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value 
expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), 
or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not 
contain any leading spaces. Only main should call print.

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()


Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py

'''

from bank import value

def test_hello():

    assert value('Hello, how are you?') == 0
    assert value('Why, hello there!') == 100 
    assert value('hello.....') == 0
    assert value('HELLO DUDE') == 0

def test_h():

    assert value('hey bud!') == 20 
    assert value('hows it going?') == 20
    assert value('why, hows it going?') == 100
    assert value('HOWDY!!!!') == 20

def test_other():

    assert value('Greetings, valued customer.') == 100 
    assert value('Good afternoon and hello!') == 100
    assert value('GEE, WELCOME IN!!') == 100 
    assert value('Whats poppin bro!') == 100