"""
Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name,
and return the birthday of that person back to them.
"""

birthdays = {'Albert Einstein': 'March 14, 1879',
             'Benjamin Franklin': 'January 17, 1706',
             'Ada Lovelace': 'December 10, 1815',
             'Elon Musk': 'June 28, 1971'}


def get_birthdays_list(birthdays_info: dict):
    """Prints birthdays from dictionary"""

    print('Welcome to the birthday dictionary. We know the birthdays of:')

    for item in birthdays_info:
        print(item)


def get_birthday_info(name: str) -> str:
    """Prints person birthday date"""

    if name in birthdays:
        print(f'{name} birthday is {birthdays[name]}')
    else:
        print(f'We don\'t now {name} birthday')


if __name__ == "__main__":
    get_birthdays_list(birthdays)
    name = input('Enter name from the list above: ')
    get_birthday_info(name)
