"""
Ask the user for a number. Depending on whether the number is
even or odd, print out an appropriate message to the user.

Extra:
Ask the user for two numbers: one number to check and
one number to divide by check. If check divides evenly
into number, tell that to user. If not, print appropriate message.
"""

try:
    number = int(input("Please enter an integer to check: "))
    check = int(input("Please enter an integer to divide: "))
except ValueError:
    print("Entered values must be integers")
else:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    if number % check == 0:
        print(f"{number} divides evenly by {check}")
    else:
        print(f"{number} does not divides evenly by {check}")
