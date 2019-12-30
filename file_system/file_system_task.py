import os
import sys

def check_counter_file():
    """Check if the file exists"""

    for dirpath, dirnames, files in os.walk('.'):
        if 'counter.txt' in files:
            handle_counter_file()
        else:
            create_file()

def handle_counter_file():
    """File handling"""

    with open('counter.txt', 'r+') as file:
        content = file.read()
        try:
            valid_content = int(content)
        except ValueError:
            return sys.exit(1)
        file.seek(0)
        file.write(str(valid_content+1))
        file.truncate()

    return sys.exit(0)


def create_file():
    """Create a file with access for all users"""

    with open('counter.txt', 'w') as file:
        file.write('1')
    os.chmod('counter.txt', 0o777)

    return sys.exit(0)


if __name__ == '__main__':
    check_counter_file()
