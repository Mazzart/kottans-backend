"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and
constructing a list, and another using sets.
"""

def remove_list_duplicates_1(a_list: list) -> list:
    """Returns initial list without duplicates"""

    return list(set(a_list))


def remove_list_duplicates_2(a_list: list) -> list:
    """Returns initial list without duplicates"""

    b_list = []
    for item in a_list:
        if item not in b_list:
            b_list.append(item)         

    return b_list


if __name__ == "__main__":
    print(remove_list_duplicates_1([1, 1, 2, 2, 3, 4, 5, 5]))
    print(remove_list_duplicates_2([10, 10, 11, 12, 12, 13, 15, 15]))
