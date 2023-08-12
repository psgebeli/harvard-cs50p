
# Ask user for their name
# Remove whitespace from str by using strip() method and 
# capitalize using title() method (first letter of each word)

name = input('What\'s your name? ').strip().title()

# Say hello to user
print(f"hello, {name}")

# Python official documentation for print function
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)