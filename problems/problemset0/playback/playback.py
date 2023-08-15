# Paul Gebeline, Problem Set 0
# Goal: implement a program in Python that prompts the user for input and then outputs that same input, 
# replacing each space with ...


def main():

    # Prompt the user
    print("This is a safe space. Say whatever you want to say.")

    # Store their input as a string 
    initial_string = input()

    # Remove whitespace to the left and right of string
    stripped_string = initial_string.strip()

    # Slow down the string by replacing spaces with ...
    slow_string = stripped_string.replace(" ", "...")

    print(slow_string)

# Call to main
main()
