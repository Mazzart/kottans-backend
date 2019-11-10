"""
Write a function that takes an ordered list of numbers and another number.
The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extra:
Use binary search.
"""
def number_search(array: list, n: int) -> bool:
    """Returns True if number in list otherwise False"""

    for item in array:
        if item == n:
            return True
    return False


def number_search_binary(array: list, n: int) -> bool:
    """Returns True if number in list otherwise False
       Binary search is used
    """
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2

        if array[middle_index] > n:
            max_index = middle_index - 1
        else:
            if array[middle_index] < n:
                min_index = middle_index + 1
            else:
                return True
    return False
            



if __name__ == "__main__":
    a = [1, 3, 5, 30, 42, 43, 500, 650]
    print(number_search(a, 42))
    print(number_search_binary(a, 29))
