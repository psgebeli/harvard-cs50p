# Paul Gebeline, Problem Set 3 
'''

INSTRUCTIONS
------------

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, 
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, 
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


 '''

def main():

    # While loop to continue prompting the user until their input passes criteria
    while True:
        try:
            # split input into two components, then convert to integers and calculate fuel fraction (to nearest int)
            x, y = input('Fraction: ').split('/') 
            n, m = int(x), int(y)
            fuel = round(n / m * 100) # round the percent to the nearest int
            if 0 <= fuel <= 1: # empty, print such and break loop
                print('E')
                break
            elif 99 <= fuel <= 100: # full, print such and break loop
                print('F')
                break
            elif n > m:
                print('The numerator must be greater than the denominator.')
                continue
            else:
                print(f'{fuel}%') # print percentage of tank full and break loop
                break
        except ZeroDivisionError: # exceptions
            print('The denominator cannot be zero.')
        except ValueError:
            print('The numerator and denominator must be integers.')

main()