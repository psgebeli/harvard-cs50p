# Paul Gebeline, Problem Set 3 

'''

INSTRUCTIONS
------------

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, 
which is arguably bad design. Dates in that format can`t be easily sorted because the date`s year comes last instead of first. 
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). 
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day 
(YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, 
“padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user`s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

'''

# Store the name of months in a list, will be used to check if month inputted is valid
months = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'
]


def main():
    
    # Loop to continue prompting user until a valid date is entered
    while True:

        # Prompt user and remove whitespace
        input_date = input('Enter a date: ').strip()

        # Call the convert function to change the date to YYYY-MM-DD format
        date = convert(input_date)
        
        # If the string is empty, print invalid and continue loop, else (if its valid) print the date and break the loop
        if date == '':
            print('Invalid entry.')
        else:
            print(date)
            break

def convert(date):

    # Create an empty string
    new_date = ''

    # If the inputted date is middle endian format (MM/DD/YYYY) (call to function)
    if is_middle_endian(date):

        # Assign strings to month, day, and year based on '/' seperators
        month, day, year = date.split('/')

        # Call is_valid function to check if the int value of month, day, and year are within normal ranges
        if is_valid(int(month), int(day), int(year)):

            # If it is valid, return a string formatted YYYY-MM-DD. .zfill(2) is used to add 0s to the beginning until string is 
            # length 2. eg '8'.zfill(2) = '08'
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
        
        # Otherwise (if its not valid), return an empty string
        else:
            return ''

    # If the inputted date is in the format Month D, YYYY (call to function)
    elif is_monthday_year(date):
        
        # Create two elements based on comma separation, where first element is the month and day (eg September 8), and 
        # the second element is the year 
        monthday, year = date.split(', ')

        # Furthermore, split the month/day element into month, day based on space seperation (September 8 --> September, 8)
        month, day = monthday.split(' ')

        # If the month is in the months list defined at the beginning of the script, convert the month string 
        # into the appropriate value based on the months position in the list. 
        # e.g 'August' = months.index('August') = 8 
        if month in months:
            month = str(months.index(month) + 1)
        
        # If the month isnt in the months list, return an empty string since its invalid input
        else:
            return ''
        
        # Again call is_valid function, and if it is valid, print YYYY-MM-DD format. Otherwise return empty string.
        if is_valid(int(month), int(day), int(year)):
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
        else:
            return ''
    
    # Return an empty string if the inputted date is neither in MM/DD/YYYY format nor Month D, YYYY format
    else: 
        return ''

# The date is in middle endian (MM/DD/YYYY) format if the first character is a number and the split method, seperated by '/', 
# creates a list of three elements. 
def is_middle_endian(date):
    return True if date[0].isnumeric() and len(date.split('/')) == 3 else False

# The date is in Month D, YYYY format if the first character is a letter, the date splits into two elements seperated by ',',
# and the first element further splits into two elements separated by a space. 

# e.g string = September 8, 2023 
# string.split(',') = ['September 8', '2023']
# string.split(',')[0].split(' ') = 'September 8'.split(' ') = ['September', '8']

def is_monthday_year(date):
    return True if date[0].isalpha() and len(date.split(', ')) == len(date.split(', ')[0].split(' ')) == 2 else False

# A particular month, day, year combo are valid if within these ranges.
def is_valid(month, day, year):
    return True if 1 <= day <= 31 and 1 <= month <= 12 and year >= 1 else False

# Call to main
main()
