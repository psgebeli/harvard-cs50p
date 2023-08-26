# Paul Gebeline, Problem Set 3 

'''

INSTRUCTIONS
------------

Suppose that you`re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user 
inputs control-d (which is a common way of ending one`s input to a program). Then output the user`s grocery list in all 
uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user`s input case-insensitively.

'''


# Empty dict to store items and number of times entered
grocery_list = {}


def main():

    # Loop to continue prompting user for item until exit.
    while True:

        try: 
            # Prompt the user for input and convert it to uppercase.
            item = input().upper()
            
            # If the item is not in the dictionary, create
            # a key/value pair of item : 1, where '1' represents the
            # amount of times the user has inputted that particular item.
            if item not in grocery_list: 
                grocery_list[item] = 1
            
            # Otherwise (if its already in the dictionary), add 1 to the value
            # since it has been entered again
            else:
                grocery_list[item] += 1
        
        # Break out of the loop if the user inputs CTRL+D (EOF) or CTRL+X+C (Keyboard Interrupt)
        except EOFError:
            break
        except KeyboardInterrupt:
            break
    
    
    # Alphabetize the items by making a list of the existing keys in grocery list,
    # then using the list sort() method to alphabetize the list
    alphabetized_items = list(grocery_list.keys())
    alphabetized_items.sort()

    # Make the alphabetized list into a dictionary with key/value pairs
    # item : value, for each item in alphabetized items, where the value is 
    # the value that was associated with that key in the original dictionary.
    alphabetized_dict = {i: grocery_list[i] for i in alphabetized_items}

    # Print the number of times item has been entered, followed by the item
    for item in alphabetized_dict:
        print(f"{alphabetized_dict[item]} {item}")

main()