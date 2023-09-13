# Paul Gebeline, Problem Set 7

'''

INSTRUCTIONS
------------

In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isnt actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address 
in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice 
it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein youre welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. 
Youre welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ...


...


if __name__ == "__main__":
    main()

Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively 
test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py


'''


# Preamble 
import re 
import sys 

# Main function just passes user input to validate() function and prints the result
def main():
    print(validate(input('IPv4 Address: ')))

# Takes an ip (string) as input
def validate(ip):

    # Store the number of sequences of digits that are correct (in #.#.#.#, all four # must be valid digits)
    num_valid = 0
    
    # If the ip contains the regular expression with four digits (\d) repeated up to 3 times, with each sequence followed by a period,
    # assign the return values of re.search to matches variable
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):

        # Store the return values in a list 
        matches_list = [matches.group(1), matches.group(2), matches.group(3), matches.group(4)]

        # For each match in the list, add 1 to num_valid if the match is between 0 and 255, otherwise add 0 
        for match in matches_list:
            num_valid += 1 if 0 <= int(match) <= 255 else 0
    
    # Return result of Boolean num_valid == 4 (True if it is a true statement, false if it is not)
    return num_valid == 4
        

if __name__ == '__main__':
    main()