# Paul Gebeline, Problem Set 4
'''

INSTRUCTIONS
------------

In The Sound of Music, there`s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” 
in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn`t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn`t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that 
the user will input at least one name. 
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, 
and n names with n-1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

'''

def main():

    # Call retrieve names function to store all inputted names
    names = retrieve_names()

    # Call the adieu function, which returns the greeting to the names, 
    # and print it after 2 new lines (so its not Name: greeting)
    print(f"\n\n{adieu(names)}")


def retrieve_names():

    # Initiate empty list
    names = []

    # Loop to continue prompting for input
    while True:

        # Try to append the inputted name to the names list
        try:

            name = input("Name: ")
            names.append(name)

        # Except if the user enters CTRL+d, then break the loop
        except EOFError:

            break 

    # Return the names list after the loop has finished
    return names


def adieu(names):
    
    
    # If the user inputs one name, return greeting to that name
    if len(names) == 1:
        return f"Adieu, Adieu, to {names[0]}"
    
    # Otherwise, return greeting to all of the names seperated by a comma+space,
    # besides the last name in the list which should be preceded by an 'and'
    else:
        final_name = names[-1]
        preceding_names = ", ".join(names[:-1])
        return f"Adieu, Adieu, to {preceding_names}, and {final_name}"

# Only execute main if this is the file being executed
if __name__ == '__main__':
    main()