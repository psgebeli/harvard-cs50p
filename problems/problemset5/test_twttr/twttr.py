# Paul Gebeline, problem set 2

'''

INSTRUCTIONS
------------

When texting or tweeting, it`s not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.

'''

def main():

    # Prompt the user 
    str = input("What would you like to say? ")

    # Call function to remove vowels 
    twitter_str = shorten(str)

    # Print result 
    print(twitter_str)

def shorten(word):

    # Define an empty string that we will populate with the modifications
    new_string = ''

    # Create a loop, iterating over each letter in the inputted string
    for letter in word:
        if letter not in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
            new_string += letter # If the letter is not a capital/lowercase vowel, add it to the new string
            # The absence of an else statement means that nothing will happen in cases where the letter 
            # is a vowel, AKA it wont be in the new string
    return new_string




if __name__ == '__main__':
    main()