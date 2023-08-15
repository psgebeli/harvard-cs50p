# Paul Gebeline, problem set 0
# Goal: fill out required functions

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    
    # Remove the $ by replacing it with an empty string
    clean_d = d.replace("$", "")

    # Return the string as a float
    return float(clean_d)
    
    

def percent_to_float(p):
    
    # Remove the % in the same fashion
    clean_p = p.replace("%", "")

    # Return the string as a float divided by 100 (to decimal form)
    return float(clean_p) / 100


main()
