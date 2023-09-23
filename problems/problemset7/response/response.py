



'''

INSTRUCTIONS
------------

In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user 
for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. 
You may not use re. And do not validate whether the email address`s domain name actually exists.

'''

from validator_collection import checkers

def main():

    # Print result of the checker function for user-entered email
    print(checker(input('Email: ')))

def checker(email):

    # Return valid if validator_collection.checkers.is_email decides the email is valid, otherwise return invalid
    return 'Valid' if checkers.is_email(email) else 'Invalid'    

if __name__ == '__main__':
    main()