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

from datetime import date 
import sys 
from num2words import num2words

def main():
    
    date = get_date(input('Birthdate: '))
    print(calculate_age(date))

def get_date(s):
    try:
        birth_date = date.fromisoformat(s)
    except ValueError:
        sys.exit('Please enter birthdate in YYYY-MM-DD format.')
    return birth_date

def calculate_age(date):

    # Calculate age in minutes based on difference between today's date and the passed-in date.
    #                       AGE IN YEARS            * HRS   * MINUTES = AGE IN MINUTES
    age_in_minutes = int((date.today() - date).days) * 24 * 60

    return f'{num2words(age_in_minutes).replace(" and ", " ")} minutes'

if __name__ == '__main__':
    main()










