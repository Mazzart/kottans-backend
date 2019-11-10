"""
Load the birthday dictionary from a JSON file on disk,
rather than having the dictionary defined in the program.
"""

import json


def get_birthdays_info(file_name: str) -> dict:
    """Returns birthday dictionary"""

    print('Welcome to the birthday dictionary. We have the following info:')

    with open(file_name, 'r') as bd:
        birthdays_info = json.load(bd)

    return birthdays_info


if __name__ == "__main__":
    print(get_birthdays_info('birthdays.json'))
