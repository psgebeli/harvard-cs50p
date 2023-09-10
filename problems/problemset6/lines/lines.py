# Paul Gebeline, Problem Set 6 

'''

INSTRUCTIONS
------------

In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, 
and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one 
command-line argument, or if the specified file`s name does not end in .py, or if the specified file does not exist, the program should 
instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) 
Assume that any line that only contains whitespace is blank.

'''

import sys 

def main():

    # Predefined usage statement to print when there are errors
    usage = 'Usage: python lines.py file_name.py'

    # Try to store the first cmd-line argument as script, except if theres an index error (no cmd-line args) then 
    # exit with usage.
    try:
        script = sys.argv[1]
    except IndexError:
        sys.exit(usage)
    
    # If the script does not end in .py or there is not only one cmd-line argument, exit with usage.
    if not script.endswith('.py') or len(sys.argv) != 2:
        sys.exit(usage)

    # Print result from call to get_lines().
    print(f"The given script has {get_lines(script)} lines.")


# Function to return number of non-commented/non-empty lines in a python script.
def get_lines(script):

    # Open the script and store stream as file 
    with open(script) as file:

        # Initialize number of lines to 0
        lines = 0 

        # For each line in the file, add 1 to lines if the line is non-empty and doesnt start with #. otherwise add 0.
        for line in file:    
            lines += 1 if (not line.isspace() and not line.strip().startswith('#')) else 0

        return lines



if __name__ == '__main__':
    main()


