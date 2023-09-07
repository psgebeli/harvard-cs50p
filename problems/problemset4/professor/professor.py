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

# Function to get the level from the user
def get_level():

    # Continue prompting for valid input until valid input is rexeived
    while True:

        # Store input as var
        level = input("Level: ")

        # If the level is 1, 2, or 3, break the loop. Otherwise, print error and restart.
        if level in ['1', '2', '3']:
            break
        else:
            print("Level outside of expected range")
    
    # Return the level as an integer
    return int(level)

# Function to create a random integer with level digits
def generate_integer(n):

    # Match statement to use different ranges of randint() depending on n 
    match n:

        # If n is 1, randint from 0 to 9 inclusive
        case 1:
            random_int = randint(0, 9)
        # Similarly
        case 2:
            random_int = randint(10, 99)
        case 3:
            random_int = randint(100, 999)

        # Otherwise raise a value error
        case _:
            raise ValueError("Available levels are 1, 2, and 3.")
    
    # Return the int
    return random_int

def main():

    # Get the level
    level = get_level()

    # Define problems as an empty dictionary
    problems = {}

    # Initialize the number of correct answers
    num_correct = 0

    # For i = 1, 2, ..., 10
    for i in range(1, 11):

        # Initialize number of tries to zero inside the loop (so it resets for each answer)
        num_tries = 0

        # Generate two randints based on level and store as x, y
        x, y = generate_integer(level), generate_integer(level)

        # Create key value pair {i: problem}, where problem is the two randints on this iteration
        problems[i] = f"{x} + {y} = "

        # While the number of tries is not 3
        while num_tries != 3:

            # Prompt the user with a problem and store their guess as an int
            guess = int(input(problems[i]))

            # If the guess is correct, break the while loop 
            if guess == x + y:
                num_correct += 1
                break

            # If the guess is incorrect, iterate number of tries and print EEE
            else:
                num_tries += 1
                print("EEE")

        # If the number of tries is 3, print the solution
        if num_tries == 3:
            print(problems[i], x + y)

        # Iterate i, moving onto the next problem 
        i += 1

    # After the for loop, print the score
    print(f"Score: {num_correct}")

if __name__ == '__main__':
    main()








        
