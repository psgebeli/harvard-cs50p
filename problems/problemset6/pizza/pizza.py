# Paul Gebeline, Problem Set 6 

'''

INSTRUCTIONS
------------

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in 
Pinocchio`s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. 

Format the table using the library`s grid format. If the user does not specify exactly one command-line argument, or if the specified 
file`s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

'''

# Preamble
from tabulate import tabulate 
import sys 
import csv 


def main():

    # Usage statement to be used for errors
    usage = 'Usage: python pizza.py csv_file.csv'

    # Try to store first cmd line arg as input, except if theres an indexerror (no args) then exit with usage
    try:
        input = sys.argv[1]
    except IndexError:
        sys.exit(usage)

    # Also exit with usage if there are more than one cmd-line arg or if its not a csv
    if len(sys.argv) != 2 or not input.endswith('.csv'):
        sys.exit(usage)

    # Empty list to store data
    data = []

    # Open the input as 'file' and define a reader from csv library 
    with open(input) as file:
        reader = csv.reader(file)

        # For each row that is read, append it to the data (reader will append each row as a list)
        for row in reader:
            data.append(row)
    
    # Tabulate the data in grid format and print the result
    print(tabulate(data, headers = 'firstrow', tablefmt = 'grid'))

        
if __name__ == '__main__':
    main()
