# Paul Gebeline, Problem Set 2

'''

INSTRUCTIONS
------------

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 
20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, 
display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and 
then outputs the number of calories in one portion of that fruit, per the FDA`s poster for fruits, which is also available 
as text. Capitalization aside, assume that users will input fruits exactly as written in the poster 
(e.g., strawberries, not strawberry). Ignore any input that isn`t a fruit.


'''

def main():

    # Prompt user 
    fruit = input("Item: ")

    # Make the input case-insensitive by converting to all lowercase
    fruit = fruit.casefold()

    # Call calorie function 
    calories = calculate_calories(fruit)

    # Print calories except if its an empty string (invalid input), then print nothing
    print("Calories:", calories) if calories != '' else print('')

def calculate_calories(item):

    # If the input matches a particular case, return the number of calories for that fruit per FDA's chart
    # Many fruits have the same calories and can thus be in the same case
    match item:
        case 'apple':
            return 130
        case 'banana':
            return 110
        case 'pear' | 'sweet cherries':
            return 100 
        case 'grapes' | 'kiwifruit':
            return 90
        case 'orange' | 'watermelon':
            return 80
        case 'plums':
            return 70
        case 'grapefruit' | 'nectarine' | 'peach':
            return 60
        case 'tangerine' | 'strawberries' | 'pineapple' | 'cantaloupe' | 'avocado':
            return 50
        case 'lime':
            return 20
        case 'lemon':
            return 15
        # Return an empty string if the input is not one of the most 20 commonly consumed fruits
        case _:
            return ''

# Call to main
main()

