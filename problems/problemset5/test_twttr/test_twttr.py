'''

INSTRUCTIONS
------------

In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten 
expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py

'''



from twttr import shorten

def main():
    test_lowercase()
    test_uppercase()
    test_novowels()

def test_lowercase():

    assert shorten('hello') == 'hll'
    assert shorten('goodbye') == 'gdby'
    assert shorten('cheesecake') == 'chsck'
    assert shorten('twitter') == 'twttr'
    assert shorten('hello1.') == 'hll1.'

def test_uppercase():
    
    assert shorten('HELLO') == 'HLL'
    assert shorten('GOODBYE') == 'GDBY'
    assert shorten('CHEESECAKE') == 'CHSCK'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('HELLO1!') == 'HLL1!'

def test_novowels():

    assert shorten('cry') == 'cry'
    assert shorten('cyst') == 'cyst'
    assert shorten('sylph') == 'sylph'
    assert shorten('rhythym') == 'rhythym'