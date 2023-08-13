# Paul Gebeline, Problem Set 0
# Goal : prompt the user for input and output it in lowercase 

def cleanstring(string_initial):
    return string_initial.casefold() 

def main():

    # Prompt the user
    print("This is a safe space. Say whatever you want to say.")

    # Store input as a string
    string_initial = input()

    # Print the result of the cleaning
    print(cleanstring(string_initial))

# Call to main
main()
