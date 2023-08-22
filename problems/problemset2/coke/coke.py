# Paul Gebeline, problem set 2 

'''

INSTRUCTIONS
------------

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn`t an accepted denomination.



'''

def main():

    # Initialize amount due
    amount_due = 50

    # Initialize the amount paid, total, over the course of the interaction
    amount_paid = 0


    while amount_due > 0:

        # Print amount due 
        print(f"Amount Due: {amount_due}")

        # Prompt user 
        insertion = int(input("Insert Coin: "))

        if insertion in [5, 10, 25]:
            amount_due -= insertion
            amount_paid += insertion
    
    # Calculate change owed
    change_owed = amount_paid - 50

    # Print change owed 
    print(f"Change Owed: {change_owed}")
        
main()
    

