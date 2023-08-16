# Paul Gebeline, Problem Set 1

'''
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You`re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker`s Guide to the Galaxy, Douglas Adams

Goal: implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) 
forty-two or forty two. Otherwise output No.

'''

def main():

    # Prompt the user and store their input 
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    # Convert the answer to all lowercase and remove extra whitespace
    answer = answer.casefold().strip()

    # Output conditional statement 
    if is_correct(answer):
        print("Yes")
    else:
        print("No")

def is_correct(statement):

    # Return true if the answer is '42', 'forty-two', or 'forty two', otherwise false
    match statement:
        case '42' | 'forty-two' | 'forty two':
            return True
        case _:
            return False

main()