"""
Take two lists and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extra:
Randomly generate two lists to test this
"""
import random

first_list = random.sample(range(100), 15)  # randomly generates list of len 15
second_list = random.sample(range(100), 20)  # randomly generates list of len 20


def common_items(a: list, b: list) -> list:
    """
    Return list of common items in two lists
    """
    
    return [i for i in set(a) if i in b]


if __name__ == "__main__":
    print(common_items(first_list, second_list))
