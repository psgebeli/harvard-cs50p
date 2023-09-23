# Paul Gebeline, Problem Set 7 

'''

INSTRUCTIONS
------------

Its not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more 
noticeable it tends to be!

In a file called um.py, implement a function called count that expects a line of text as input as a str and returns, as an int, 
the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. 
For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should 
return 0.

Structure um.py as follows, wherein youre welcome to modify main and/or implement other functions as you see fit, but you may not 
import any other libraries. Youre welcome, but not required, to use re and/or sys.

def main():
    print(count(input("Text: ")))
def count(s):
    ...
...
if __name__ == "__main__":
    main()


Either before or after you implement count in um.py, additionally implement, in a file called test_um.py, three or more functions that 
collectively test your implementation of count thoroughly, each of whose names should begin with test_ so that you can execute your 
tests with:

pytest test_um.py

'''

import re 
import sys 

def main():

    # Prompt for input and print result of count function
    print(count(input('Text: ')))

def count(s):

    # Initialize number of ums
    ums = 0 

    # Each time the pattern \bum\b (um as standalone word) followed by a space or punctuation is matched, add 1 to ums and return after
    for match in re.finditer(r'\bum\b(?:[:punct:]|\s)*', s, re.IGNORECASE):
        ums += 1
    return ums 

if __name__ == '__main__':
    main()