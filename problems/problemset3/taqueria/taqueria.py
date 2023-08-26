# Paul Gebeline, problem set 3

'''

INSTRUCTIONS
------------

One of the most popular places to eat in Harvard Square is Felipe`s Taqueria, which offers a menu of entrees, 
per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, 
one per line, until the user inputs control-d (which is a common way of ending one`s input to a program). After each inputted 
item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user`s input case insensitively. Ignore any input that isn`t an item. Assume that every item on the menu will be 
titlecased.
'''

# Define the dictionary provided in instructions
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    # Initialize the total amount paid by user
    total = 0

    # Loop to continue prompting user until they are done ordering
    while True:

        try:

            # Prompt user
            item = input("What would you like to order from the Taqueria? ").title()

            # If the item ordered is defined in the dictionary, add its price to the total, and print current total. Prompt again.
            if item in menu:
                total += menu[item]
                print(f"Your total is ${total:.2f}. What else would you like to order? ")

            # If the item is not in the menu, say its invalid.
            else:
                print("Invalid item.")
        # If the user exits via CTRL+D, aka an EOFError, thank them for their business and break the loop.
        except EOFError:
            print("Thanks for your business.")
            break
            
# Call to main
main()