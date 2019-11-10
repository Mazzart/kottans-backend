"""
Take two lists and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python
"""
import random


# Random generation of two lists
try:
    first_length = int(input("The length of the first list (<100): "))
    second_length = int(input("The length of the second list (<100): "))
    first_list = random.sample(range(100), first_length)
    second_list = random.sample(range(100), second_length)
except ValueError:
    print("Check entered values")


def common_in_list(list_1: list, list_2: list) -> list:
    """Returns a list that contains common elements in two lists"""
    
    return [i for i in list_1 if i in list_2]


if __name__ == "__main__":
    try:
        print(common_in_list(first_list, second_list))
    except NameError:
        print("Please, try again")
