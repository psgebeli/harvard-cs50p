# Paul Gebeline, Problem Set 6

'''

INSTRUCTIONS
------------

In a file called scourgify.py, implement a program that:

--Expects the user to provide two command-line arguments:
    1. the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    2. the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

--Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a 
first name and last name.

--If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit 
with an error message.

'''

# Preamble
import csv 
import sys

# Usage statement for error printing
usage = 'Usage: python scourgify.py input.csv output.csv'

def main():

    # Try to assign the two command line arguments to variables csv_in and csv_out, respectively (input/output file name)
    try:
        csv_in = sys.argv[1]
        csv_out = sys.argv[2]

    # Except if theres an index error (less than two args), then exit with usage
    except IndexError:
        sys.exit(usage)
    
    # Also exit with usage if there are more than two args, or the args dont end in .csv
    if len(sys.argv) != 3 or not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('csv'):
        sys.exit(usage)

    # Call read_csv file to read the input csv and return a list of dictionaries for each student
    students = read_csv(csv_in)

    # Call split to construct a new list with dictionaries where the name key is split into first, last keys
    students_new = split(students)

    # Use this new list of dictionaries to write a csv file using write_csv funct
    write_csv(students_new, csv_out)
    

# Take csv file as input, read it, and store data in a list called students with dictionary for each student
def read_csv(file):

    # Initialize empty list
    students = []

    # Open the file and store the stream as file 
    with open(file) as file:

        # Define a reader from csv module that reads each row as a dictionary, where the keys are based on the first row
        reader = csv.DictReader(file)

        # For each row, append the dictionary from the reader to students
        for row in reader:
            students.append(row)

    # Return the completed list 
    return students

# Take list of students as input and return a new list where the dictionary's key 'name' is split into first/last
def split(students):

    # Initialize new list
    students_new = []

    # For each student (dictionary)
    for student in students:

        # Split the value for 'name' into last, first based on ', ' seperator
        last, first = student['name'].split(', ')

        # Append a new dictionary with keys 'first', 'last', 'house' to the list
        students_new.append({'first': first, 'last' : last, 'house' : student['house']})

    # Return the completed list
    return students_new 


# Takes students list as input, and the name of the output file to be written
def write_csv(students, outfile):

    # Create a file called outfile and open it in write mode, store stream as 'file'
    with open(outfile, 'w') as file:

        # Define a dictionary writer from csv module with keys 'first', 'last', 'house'
        writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])

        # Write the first row, which will be the field names 
        writer.writeheader()

        # For each student, write a row based on their dictionary
        for student in students:
            writer.writerow(student)



if __name__ == '__main__':
    main()

