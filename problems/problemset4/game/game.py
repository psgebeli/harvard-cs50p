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

    # Define a string since it will be printed a lot.
    error = "Please input a positive integer."

    # Loop to continue prompting for a valid level.
    while True:

        # Try to store the inputted level as an integer
        try:
            level = int(input("Level: "))

            # If the level is out of range, print the error and continue the loop. If its within range, break the loop.
            if level <= 0:
                print(error)
            else:
                break
        
        # Except if there is a value error (non-integer inputted), then print the error and continue the loop.
        except ValueError:
            print(error)
    
    # Generate a random int between 1 and the level (randint function is inclusive)
    random_int = randint(1, level)

    # While loop to continue running until the guess matches the level
    while True:

        # Try to store the inputted guess as an integer
        try:
            guess = int(input("Guess: "))

            # If the guess is correct (via call to function), print just right and break the loop.
            if compare(guess, random_int) == "Just right!":
                print("Just right!")
                break

            # Else if the guess is outside of range (greater than level), print an error msg and continue loop.
            elif guess > level:
                print("Ensure your guess is within the level range.")
            
            # Otherwise (if the guess is a valid int), print the return value of compare() funct and continue loop 
            else:
                print(compare(guess, random_int))
        
        # Except if theres a value error, print the error 
        except ValueError:
            print(error)
        
# Function to compare two integers
def compare(n, m):
    if n > m:
        return "Too large!"
    elif n < m:
        return "Too small!"
    else:
        return "Just right!"
    
# Call to main if this is the file being executed
if __name__ == '__main__':
    main()