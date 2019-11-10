"""
Write one line of Python that takes the list a and 
makes a new list that has only the even elements of this list in it.
"""
import random

a = random.sample(range(100), 10)

new_list = [x for x in a if x % 2 == 0]

print(new_list)
