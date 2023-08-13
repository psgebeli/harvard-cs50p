# Paul Gebeline, Problem Set 0
# Goal: implement a program in Python that prompts the user for input and then outputs that same input, 
# replacing each space with ...


def main():

    # Prompt the user
    print("This is a safe space. Say whatever you want to say.")

    # Store their input as a string and split it 
    initial_string = input().split(" ")

    # Print the string separated by '...' rather than ' '
    print(initial_string, sep='...')

# Call to main
main()
