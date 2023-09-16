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
    
    time_range = input("When do you work? ")
    print(convert(time_range))


def convert(s):

    if matches := re.search(r"(\d\d?)(:\d\d)?\s(AM|PM)\sto\s(\d\d?)(:\d\d)?\s(AM|PM)", s):


        start_hour, start_meridiem = int(matches.group(1)), matches.group(3)
        stop_hour, stop_meridiem = int(matches.group(4)), matches.group(6)

        start_minutes = int(matches.group(2).replace(':', '')) if matches.group(2) else 0
        stop_minutes = int(matches.group(5).replace(':', '')) if matches.group(5) else 0

        start_decimal = start_hour + start_minutes / 60 if start_minutes else start_hour
        stop_decimal = stop_hour + stop_minutes / 60 if stop_minutes else stop_hour

        match start_meridiem:
            case 'AM':
                if 12.0 <= start_decimal < 13.0:
                    start24 = start_decimal - 12.0
                else:
                    start24 = start_decimal
            case 'PM':
                if 1.0 <= start_decimal < 12.0:
                    start24 = start_decimal + 12.0
                else:
                    start24 = start_decimal
        
        match stop_meridiem:
            case 'AM':
                if 12.0 <= stop_decimal < 13.0:
                    stop24 = stop_decimal - 12.0
                else:
                    stop24 = stop_decimal
            case 'PM':
                if 1.0 <= stop_decimal < 12.0:
                    stop24 = stop_decimal + 12.0
                else:
                    stop24 = stop_decimal


        # Format the time with a colon between hours and minutes
        start24_str = f'{int(start24):02}:{int((start24 % 1) * 60):02}'
        stop24_str = f'{int(stop24):02}:{int((stop24 % 1) * 60):02}'

        return f'{start24_str} to {stop24_str}'
    else:
        raise ValueError("invalid input")
        
        
if __name__ == '__main__':
    main()