"""
Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them.
"""
def fibonacci_numbers(n: int) -> list:
    """Returns Fibonacci sequence"""

    sequence = []
    
    if n < 1:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        a, b = 1, 1
        while n > 0:
            sequence.append(a)
            a, b = b, a + b
            n -= 1          

    return sequence


if __name__ == "__main__":
    try:
        n = int(input("How many Fibonacci numbers to generate: "))
        print(fibonacci_numbers(n))
    except ValueError:
        print("Entered value must be integer.")
