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
    
    # Prompt user for input, then print the result of convert() funct.
    time_range = input("When do you work? ")
    print(convert(time_range))


def convert(s):

    # If matches can be assigned to the return values of re.search, where the regex 
    # picks out a string of the form Hh:mm AM/PM to Hh:mm AM/PM, where uppercase -> required, lowercase -> optional
    if matches := re.search(r"(\d\d?)(:\d\d)?\s(AM|PM)(\sto\s)(\d\d?)(:\d\d)?\s(AM|PM)", s):

        # Then store the hours of beginning/end of shift on 12 hr scale, as well as the AMs or PMs 
        # Hours as ints as they will be used to convert to 24 hr scale
        start_hour_12, start_meridiem = int(matches.group(1)), matches.group(3)
        stop_hour_12, stop_meridiem = int(matches.group(5)), matches.group(7)

        # Store the minutes as the return value minus the :, or '00' if there are no minutes entered
        start_minutes = matches.group(2).replace(':', '') if matches.group(2) else '00'
        stop_minutes = matches.group(6).replace(':', '') if matches.group(6) else '00'

        # Error checking for minutes or hours outside of expected range
        if not 0 <= int(start_minutes) < 60 or not 0 <= int(stop_minutes) < 60:
            raise ValueError("Invalid minutes")
        elif not 1 <= start_hour_12 <= 12 or not 1 <= stop_hour_12 <= 12:
            raise ValueError("Invalid hour")
        else: 
            pass

        # If the meridiem is AM, hour in 24 scale is 0 if hour is 12, otherwise its the same
        match start_meridiem:
            case 'AM':
                if start_hour_12 == 12:
                    start_hour_24 = 0
                else:
                    start_hour_24 = start_hour_12
        # If it is PM, then the hour gets 12 added unless the hour is 0 or 12 (then its the same)
            case 'PM':
                if 1.0 <= start_hour_12 < 12.0:
                    start_hour_24 = start_hour_12 + 12.0
                else:
                    start24 = start_hour_12
        
        # Similarly for stopping time 
        match stop_meridiem:
            case 'AM':
                if stop_hour_12 == 12:
                    stop_hour_24 = 0
                else:
                    stop_hour_24 = stop_hour_12
            case 'PM':
                if 1.0 <= stop_hour_12 < 12.0:
                    stop_hour_24 = stop_hour_12 + 12.0
                else:
                    stop_hour_24 = stop_hour_12

        # Round hour to nearest int (gets rid of decimal) and store it as a string, then fill to the left with 0s until there are 2 digits
        # e.g 7.zfill(2) = 07
        start_hour_24 = str(round(start_hour_24)).zfill(2)
        stop_hour_24 = str(round(stop_hour_24)).zfill(2)

        # Return the string in the 24 hour format (minutes unchanged)
        return f'{start_hour_24}:{start_minutes} to {stop_hour_24}:{stop_minutes}'

    # Otherwise, if the regex doesnt have return values, raise a valueerror
    else:
        raise ValueError('Invalid input')
        
        
if __name__ == '__main__':
    main()