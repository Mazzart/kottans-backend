"""
Load that JSON file from disk, extract the months of all the birthdays,
and count how many scientists have a birthday in each month.
"""
import json
from collections import Counter


def get_birthdays_info(file_name: str) -> dict:
    """Returns birthday dictionary"""

    with open(file_name, 'r') as bd:
        birthdays_info = json.load(bd)

    return birthdays_info


def count_birthday_months(birthdays: dict):
    """Returns dictionary with the months counted"""

    birthday_months = []

    for birthday in birthdays['birthdays']:
        birthday_months.append(birthday['date'].split()[0])

    months_count = Counter(birthday_months)
    return dict(months_count)


if __name__ == "__main__":
    info = get_birthdays_info('birthdays.json')
    print(count_birthday_months(info))
