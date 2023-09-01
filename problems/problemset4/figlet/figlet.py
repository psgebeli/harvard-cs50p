# Paul Gebeline, Problem Set 4 

'''

INSTRUCTIONS
------------

FIGlet, named after Frank, Ian, and Glen`s letters, is a program from the early 1990s for making large letters out of ordinary text, 
a form of ASCII art:
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/

Among the fonts supported by FIGlet are those at figlet.org/examples.html. FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

1. Expects zero or two command-line arguments:
    Zero if the user would like to output text in a random font.
    Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
    and the second of the two should be the name of the font.
2. Prompts the user for a str of text.
3. Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, 
the program should exit via sys.exit with an error message.

'''

# Preamble 
import sys as s 
import pyfiglet as pf

def main():
   
   # If there are two arguments passed and the second argument is either -f or --font
    if len(s.argv) == 3 and s.argv[1] in ('-f', '--font'):
      
        # Try to execute a test of pyfiglet. Except if the font is invalid, then exit
        # This quits the program immediately if the font is invalid, rather than after 
        # text is inputted.
        try:
            pf.figlet_format("hello world", font=s.argv[2])
        except pf.FontNotFound:
            s.exit("Ensure your font is supported by pyfiglet.")
        
        # If no exception is raised, prompt for input and print result
        text = input("Enter text: ")
        print(pf.figlet_format(text, font=s.argv[2]))
    
    # Else if there are no arguments passed
    elif len(s.argv) == 1:
       
       # Similarly prompt for input and print it, but with no font arg (random)
        text = input("Enter text: ")
        print(pf.figlet_format(text))
    
    # Otherwise, print a usage statement 
    else:
        s.exit("Usage: python figlet.py [-f | --font] [font_name]")

# Call to main
main()