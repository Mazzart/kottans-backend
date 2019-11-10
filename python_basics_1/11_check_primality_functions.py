"""
Ask the user for a number and determine whether the number is prime or not.
"""

def is_prime(n: int):
    """Return True is n is prime, False otherwise"""
    
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for number in range(2, n):
            if n % number == 0:
                return False

    return True


if __name__ == "__main__":
    try:
        number = int(input("Enter integer number: "))
        print(is_prime(number))
    except ValueError:
        print("Entered number must be integer.")
