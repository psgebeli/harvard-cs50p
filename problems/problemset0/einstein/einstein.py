# Paul Gebeline, Problem set 0
# Goal: prompt user for m (in kg) and return E (in J) via E=mc^2

def calculate_energy(m):

    # Store the speed of light as a constant (m/s)
    c = 300000000

    # Calculate the energy and return it
    return m * pow(c, 2)


def main():

    # Greet the user
    print("Hello, this program will calculate the rest energy of a mass m.")

    # Prompt the user for m and store their response as an integer
    m = int(input("What is the mass m in kg? "))

    # Do the calculation and store the output 
    E = calculate_energy(m)

    # Print output
    print(f"The energy of this object is {E} Joules.")


# Call to main
main()