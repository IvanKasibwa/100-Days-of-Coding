# Define a function to emulate raw_input in Python 3
def raw_input(prompt):
    return input(prompt)

# Taking input from the user
user_input = raw_input("Enter something: ")

# Printing the input
print("You entered:", user_input)
