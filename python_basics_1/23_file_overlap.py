"""
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has a list of all
prime numbers under 1000, and the other .txt file has a list of
happy numbers up to 1000.
"""


def files_overlap(file_1: str, file_2: str) -> list:
    with open(file_1, "r") as numbers:
        first_list = []
        number = numbers.readline()
        while number:
            number = int(number.strip())
            first_list.append(number)
            number = numbers.readline()

    with open(file_2, "r") as numbers:
        second_list = []
        number = numbers.readline()
        while number:
            number = int(number.strip())
            second_list.append(number)
            number = numbers.readline()

    return [num for num in first_list if num in second_list]


if __name__ == "__main__":
    print(files_overlap("list_of_numbers_1.txt", "list_of_numbers_2.txt"))
