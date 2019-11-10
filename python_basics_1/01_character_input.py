"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.
"""

import datetime


try:
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    bd_this_year = input("If you have bd this year enter 'YES' else 'NO': ")
    now = datetime.datetime.now()
except ValueError:
    print("Check entered values")
    

def year_message(name: str, age: int, birthday_this_year: str):
    """Program prints when you will be 100 years old"""

    if age >= 100:
       print(f"{name}, you are already 100 years old.")
    else:
        if bd_this_year.lower() == "yes":
            year = (100 - age) + now.year
        else:
            year = (99 - age) + now.year
        print(f"{name}, you will be 100 years old in {year}")


if __name__ == "__main__":
    try:
        year_message(name, age, bd_this_year)
    except NameError:
        print("Please, try again")
