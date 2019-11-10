"""
Write a program that takes a list of numbers and makes a new list
of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
a = [5, 10, 15, 20, 25]

def first_last_item(input_list: list) -> list:
    """Returns first and last elements of the given list"""

    if len(input_list) > 1:
        return [input_list[0], input_list[-1]]
    else:
        return []

if __name__ == "__main__":
    print(first_last_item(a))
