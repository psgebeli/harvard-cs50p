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

    # Initialize a number that will have 1 added to it for each criteria passed
    score = 0

    score += 1 if s[0].isalpha() == s[1].isalpha() == True else 0 

    score += 1 if 2 <= len(s) <= 6 else 0

    score += 1 if numbers_correct(s) else 0

    score += 1 if s.alnum() else 0

    return True if score == 4 else False

def numbers_correct(s):

    ???


            

main()