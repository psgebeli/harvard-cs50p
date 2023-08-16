# Paul Gebeline, Problem Set 1 

'''

INSTRUCTIONS
------------

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100
to anyone who isn`t greeted with a “hello.” Kramer is instead greeted with a “hey,”
which he insists isn`t a “hello,” and so he asks for $100. The bank`s manager proposes 
a compromise: “You got a greeting that starts with an `h,` how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” 
(but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the 
user`s greeting, and treat the user`s greeting case-insensitively.

'''

def main():

    # Prompt user, store input as string
    greeting = input("How would you like to greet Mr. Kramer? ")

    # Make the response lowercase and ignore leading whitespace
    greeting = greeting.casefold().lstrip()

    # Call the determine price function to determine how much compensation is owed based on the greeting
    price = determine_price(greeting)

    # Tell the user what they have earned
    print(f"Congratulations, you have earned ${price}.")


def determine_price(statement):

    # Use the startswith() string method to determine how much is owed based on the greeting, in dollars
    if statement.startswith('hello'):
        return 0 
    # Note that the elif statement is only ran if the string fails the first if statement
    # so a greeting 'hello' may start with h, but it wont return 20 because it doesnt get to
    # this point in the program.
    elif statement.startswith('h'):
        return 20 
    else:
        return 100

main()