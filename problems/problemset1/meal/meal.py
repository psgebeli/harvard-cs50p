# Paul Gebeline, Problem Set 1 

'''

INSTRUCTIONS
------------
Suppose that you`re in a country where it`s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
and dinner between 18:00 and 19:00. Wouldn`t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it`s breakfast time, lunch time, 
or dinner time. If it`s not time for a meal, don`t output anything at all. Assume that the user`s input will be formatted
in 24-hour time as #:## or ##:##. And assume that each meal`s time range is inclusive. 
For instance, whether it`s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it`s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time,
a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" 
(i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).


def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()

'''

def main():
    
    # Prompt the user for the current time 
    answer = input("What time is it? ")

    # Convert the input to a floating point decimal representing the number of hours
    # and based on whether it was inputted in 12hr or 24hr time
    if answer.endswith('m.'): # whether its a.m. or p.m. both cases end in .m, implying 12 hr time
        num_hours = convert_12hr(answer)
    else:
        num_hours = convert(answer)

    # Conditional loop to determine if its time to eat a meal
    if 7.0 <= num_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= num_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= num_hours <= 19.0:
        print("dinner time")
    else:
        quit


def convert(time):

    # Split the time ##:## or #:## into 2 elements
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Change minutes out of 60 to a decimal out of 100 according to 
    # minutes / 60 = minutes_outof_100 / 100 =====> minutes_outof_100 = 100*minutes/60 = 5/3*minutes
    # and minutes_as_decimal = minutes_outof_100 / 100 = 5/3 * minutes / 100 = 5/300 * minutes = 1/60 * minutes = minutes / 60
    minutes_as_decimal = float(minutes / 60)

    # If we have 8 hours and 0.77 of an hour, then we have 8 + 0.77 = 8.77 hours
    # So return the sum of the hours and the decimal representing the minutes
    return hours + minutes_as_decimal
    
# define a seperate function for conversion if the time is inputted in 12 hr format
def convert_12hr(time):

    # Split the time #:##/##:## a.m./p.m. into 2 elements
    time_12hr, meridiem = time.split()

    # Furthermore, split the 12 hour time in the same fashion
    time_12hr_converted = convert(time_12hr)

    # Adjust the 12 hour time to 24 hour time based on the meridiem (am or pm)
    # This set of conditionals can seem odd, but it is how we transition between the time systems in our heads.
    # Between 1 pm and 11:59 pm, add 12 hrs, and between 12 am and 12:59 am, subtract 12 hours
    # otherwise (e.g between 12pm and 1 pm, and between 1am to 1159 am, its the same in both systems)
    match meridiem:
        case 'a.m.':
            if 12.0 <= time_12hr_converted < 13.0:
                time_24hr = time_12hr_converted - 12.0
            else:
                time_24hr = time_12hr_converted
        case 'p.m.':
            if 1.0 <= time_12hr_converted < 12.0:
                time_24hr = time_12hr_converted + 12.0
            else:
                time_24hr = time_12hr_converted
    
    return time_24hr

if __name__ == '__main__':
    main()
