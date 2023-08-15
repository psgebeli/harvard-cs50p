# Paul Gebeline, Problem Set 0 
# Goal: prompt user for a string and replace :( / :) with emojis

def convert(initial_string):

     # Remove whitespace to the left and right of string
    stripped_string = initial_string.strip()

    # Replace :) with 🙂
    happy_string = initial_string.replace(":)", "🙂")

    # Replace :( with 🙁
    emotionally_neutral_string = happy_string.replace(":(", "🙁")

    return emotionally_neutral_string

def main():

    # Prompt the user and store input as a string
    initial_string = input("This is a safe space. Say whatever you want to say. ")

    # Convert their input and store it as a string
    converted_string = convert(initial_string)

    # Print the result
    print(converted_string)

main()
   
