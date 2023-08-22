# Problem Set 2, Paul Gebeline

'''

INSTRUCTIONS
------------

In a file called camel.py, implement a program that prompts the user for the name of a variable
 in camel case and outputs the corresponding name in snake case. Assume that the user`s input 
 will indeed be in camel case.
 
'''

def main():

    # Prompt user 
    camel = input("Variable name in camel case: ")

    # Call to convert()
    snake = convert(camel)

    # Print result
    print(f"Variable name in snake case: {snake}")

def convert(string):
    
    # Create empty string 
    newstring = ''

    # Loop over letters in the input string 

    for letter in string:
        if letter != letter.casefold(): # AKA, if the letter is upper case
            letter = letter.casefold() # Make the letter lowercase
            newstring += '_' # Add an underscore BEFORE adding the updated letter
        newstring += letter # Add updated letter 
    # After doing this for each letter, return the string
    return newstring
        
main()