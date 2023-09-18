import pytest 
from um import count 


def test_empty():
    assert count('') == 0

def test_substrings():
    assert count('that looks yummy') == 0 
    assert count('Make sure to bring an umbrella!') == 0 

def test_punctuation():
    assert count('Um, hello.') == 1
    assert count('Um... Hello') == 1
    assert count('Um! What are you doing?') == 1
    assert count('I um dont know what to do') == 1
