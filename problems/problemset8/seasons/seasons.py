# Paul Gebeline, Problem Set 8 

'''

INSTRUCTIONS
------------

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and 
then prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like 
the song from Rent, without any 'and' between words. Since a user might not know the time at which they were born, assume, 
for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. 

In other words, even if the user runs the program at noon, assume that its actually midnight, on the same date. Use datetime.date.today 
to get todays date, per docs.python.org/3/library/datetime.html#datetime.date.today.



'''

# Preamble
from datetime import date 
import sys 
import inflect 


def main():
    
    # Call get_date function to store input as date object from datetime library
    date = get_date(input('Birthdate: '))

    # Calculate the age of that date object by calling calculate age function, and print the result
    print(calculate_age(date))


def get_date(s):

    # Try to convert the string to a date object and store the result, except if theres a ValueError (invalid date/string),
    # then exit with sys
    try:
        birth_date = date.fromisoformat(s)
    except ValueError:
        sys.exit('Please enter birthdate in YYYY-MM-DD format.')

    # Return the date object
    return birth_date



def calculate_age(date):

    # Initialize inflect engine 
    p = inflect.engine()

    # Calculate age in minutes based on difference between today's date and the passed-in date.
    #                       AGE IN YEARS            * HRS   * MINUTES = AGE IN MINUTES
    age_in_minutes = int((date.today() - date).days) * 24 * 60

    # Return a f string, where we use the number_to_words method from the inflect engine to translate an integer (the age in minutes)
    # to words, which returns a string. Then on that string, replace ' and ' with ' ' (to effectively remove any and instances)
    # and capitalize the first letter. Follow this with the word minutes, to yield something like 
    #                               'Forty two minutes'
    return f'{p.number_to_words(age_in_minutes).replace(" and ", " ").capitalize()} minutes'

if __name__ == '__main__':
    main()










