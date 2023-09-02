# Paul Gebeline, Problem Set 4 

'''

INSTRUCTIONS
------------

I`m thinking of a number between 1 and 100…

What is it? In a file called game.py, implement a program that:

Prompts the user for a level, n.
    If the user does not input a positive integer, the program should prompt again.

Randomly generates an integer between 1 and n, inclusive, using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.

'''

from random import randint
def main():

    level = get_level()
    check_guess(level)



def get_level():
    
    while True:
        level = int(input("Level: "))
        integer = randint(1, level)
        check_guess(integer)
        if level >= 0:
            break
        else:
            pass

def check_guess(n):

    m = randint(1, n)

    while True:
        guess = int(input("Guess: "))
        if guess < m:
            print("Too small!")
        elif guess > m:
            print("Too big!")
        else:
            print("Just right!")
            break

if __name__ == '__main__':
    main()

