"""
Implement a function that takes as input three variables, and returns
the largest of the three. Do this without using the Python max() function
"""

def max_of_three(a, b, c):
    """Return one largest variable"""

    max_value = 0

    if a > b:
        if a > c:
            max_value = a
        else:
            max_value = c
    else:
        if b > c:
            max_value = b
        else:
            max_value = c

    return max_value


if __name__ == "__main__":
    print(max_of_three(1, 3, 7))
    print(max_of_three(10.5, 10.1, 10.7))
    print(max_of_three(5, 5, 1))
