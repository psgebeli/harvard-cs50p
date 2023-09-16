# Paul Gebeline, Problem Set 7

'''

INSTRUCTIONS
------------

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the 
corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that 
there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM 
specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM


Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid 
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someones hours will start ante meridiem and end post meridiem; 
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein youre welcome to modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. Youre welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...

...

if __name__ == "__main__":
    main()

Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, 
three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with 
test_ so that you can execute your tests with:

pytest test_working.py


'''

# Preamble 
import re 
import sys 

def main():
    ...

def convert(s):

    if matches := re.search(r"^(\d\d?)(:\d\d)?\s(AM|PM)\sto(\d\d?)(:\d\d)?\s(AM|PM)$", s):
        start_hour, start_minutes, start_meridiem = matches.group(1), matches.group(2).replace(':', ''), matches.group(3)
        stop_hour, stop_minutes, stop_meridiem = matches.group(4), matches.group(5).replace(':', ''), matches.group(6)
        
