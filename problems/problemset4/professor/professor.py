# Paul Gebeline, Problem Set 4 

'''

INSTRUCTIONS
------------

In a file called professor.py, implement a program that:

-Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.

-Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer 
with n digits. No need to support operations other than addition (+).

-Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 
    -If the user has still not answered correctly after three tries, the program should output the correct answer.

-The program should ultimately output the user`s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level 
and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or 
raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()

'''

# Preamble 

from random import randint 

def main():
    ...

def get_level():

    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            break
        else:
            print("Level outside of expected range")
    
    return level 

def generate_integer(n):

    match n:
        case '1':
            random_int = randint(0, 9)
        case '2':
            random_int = randint(10, 99)
        case '3':
            random_int = randint(100, 999)
        case _:
            raise ValueError("Available levels are 1, 2, and 3.")
    return random_int

def main():

    # Pseudo code 

    # Get level 
    # Print the first problem with two calls to random.
        # Prompt input 
        # if input is correct, print the next problem 
        # if input is incorrect and num_tries <= 3, print 'EEE'
        # if input is incorrect and num_tries = 3, print result and next problem 

    level = get_level()

    problems = {}

    num_tries = 0

    for i in range(1, 11):
        x, y = generate_integer(level), generate_integer(level)
        problems[i] = f"{x} + {y} = "
        while num_tries != 3:
            guess = input(problems[i])
            if guess == x + y:
                break
            else:
                pass
        
        i += 1

if __name__ == '__main__':
    main()








        
