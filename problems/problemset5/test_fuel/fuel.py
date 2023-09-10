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

    
    # Store input as a fraction
    fraction = input('Fraction: ')

    # Try to convert it and print the gauge result via function calls, except if there are errors
    try:
        fuel = convert(fraction)
        print(gauge(fuel))
    except ZeroDivisionError:
        print("cant divide by 0")
    except ValueError:
        print("numerator and denominator must be ints with num > denom")

# Convert a fraction (str) to an integer, or None if there are errors
def convert(fraction):

    # Try to split the input and convert to ints
   
    x, y = fraction.split('/')
    n, m = int(x), int(y)

        # Raise a value error if the numerator is greater than the denominator
    if n > m and m != 0:
        raise ValueError
    
    # Otherwise return the integer as a percentage
    return round(n / m * 100)

   
# Convert an integer to a fuel gauge reading
def gauge(integer):

    # If the integer is between 0 and 1, return E
    if 0 <= integer <= 1: 
        return('E')
    
    # Else if the integer is between 99 and 100, return F
    elif 99 <= integer <= 100:
        return('F')
    
    # Otherwise, return a format string representing the int as a percent
    else:
        return(f'{integer}%')


if __name__ == '__main__':
    main()