# Paul Gebeline, Problem Set 1

'''

INSTRUCTIONS
------------

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. 
But let`s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user`s input will be formatted as x y z, with one space between x and y and
one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

'''

def main():

    # Prompt the user for an expression
    expression = input("Please enter an arithmetic expression: ")

    # Remove whitespace 
    expression = expression.strip()

    # Split the expression into x, operator, and y (i like to be different) based on the input 
    # split(' ', 3) means break the string into elements that are seperated by a space, with a maximum of 3 elements
    x, operator, y = expression.split(' ', 3)

    # Convert x and y into integers 
    x = int(x)
    y = int(y)

    # Store the answer via a call to the calculate() function
    answer = calculate(x, operator, y)

    # Print the answer formatted to one decimal point 
    print(f"{answer:.1f}")

def calculate(n, operator, m):

    match operator:
        case '+':
            return float(n+m)
        case '-':
            return float(n-m)
        case '*':
            return float(n*m)
        case '/':
            return float(n/m)

main()
