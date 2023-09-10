# Paul Gebeline, Problem set 2

'''

INSTRUCTIONS
------------

In Massachusetts, home to Harvard University, it`s possible to request a vanity license plate for your car, 
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, 
AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a `0`.”
“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid
if meets all of the requirements or Invalid if it does not. Assume that any letters in the user`s
input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all 
requirements and False if it does not. Assume that s will be a str. You`re welcome to implement additional functions 
for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()


'''

def main():
    
    # Prompt user for their vanity plate name 
    plate = input("Plate: ")

    # Call is_valid function to determine if it meets MS vanity plate requirements, and print whether it does or does not
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    '''
    Funct to determine if an inputted plate number is valid. The logic is to check if the plate
    satisfies each of the 4 rules. But, if it fails any rule, it is automatically invalid 
    and doesn't require the subsequent rule checks, so false is returned.

    String methods used in this code:

    string.isalpha(): return True if string consists of only letters
    string.isnumeric(): return True if string consists of only numbers
    string.isalnum(): return True if string is alphanumeric, AKA contains nothing besides letters and numbers
    string.startswith(x): return True if string starts with x (x can be anything)

    '''

    # Rule 1: Between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False
    
    # Rule 2: First two characters must be letters
    if not s[0].isalpha() == s[1].isalpha() == True:
        return False
    
    # Rule 3: Numbers cant be in the middle (call to custom function)
    if not numbers_correct(s):
        return False
    
    # Rule 4: No punctuation 
    if not s.isalnum():
        return False

    # If it got through all of the checks, its valid, so return True
    return True

def numbers_correct(s):
    
    # The numbers follow the numeric rules if they dont start with a 0 and dont have middle numbers (call to below functions)
    return True if not starts_with_zero(s) and not middle_numbers(s) else False

def starts_with_zero(s):

    # Function to determine if a sequence of numbers from the input starts with a zero

    # Initialize an empty string, to be populated with the numbers in the input
    numbers = ''

    # For loop to populate numbers string with all of the numbers from the input (ignore first 2 characters since they must be letters)
    for i in range(2, len(s)):

        # Add the character to the numbers string if its a number, otherwise add empty string
        numbers += s[i] if s[i].isnumeric() else ''

    # Starts_with_zero is True if numbers string starts with a 0, otherwise its false
    return True if numbers.startswith('0') else False 

def middle_numbers(s):

    # Function to determine if there are any letters between numbers

    # Call to function to determine the amount of numbers in the input
    numbers_present = amount_of_numbers(s)

    # For each index beyond the first two (but not the last one since we are considering the subsequent element) 
    for j in range(2, len(s)-1):

        # if the jth character is a number but the subsequent element is a letter
        if s[j].isnumeric() and s[j+1].isalpha():

            # Then there are middle numbers
            return True 
        
    # If the last element is a number and its preceding character is a letter, AND there is more than one number
    if s[len(s)-1].isnumeric() and s[len(s)-2].isalpha() and numbers_present > 1:

        # Then there are middle numbers
        return True
    
    # Return false if the string passed all of this function's criteria, since that means there are no middle numbers
    return False 

def amount_of_numbers(s):

    # Function to return the amount of numbers in the input, mainly used for the function middle_letters

    # Initialize an empty string and the amount of numbers
    numbers = ''
    amount_of_numbers = 0 

    # For each character in the string, add 1 to amount_of_numbers if its a number, otherwise add 0
    for char in s:
        amount_of_numbers += 1 if char.isnumeric() else 0
    return amount_of_numbers

    
if __name__ == '__main__':
    main()