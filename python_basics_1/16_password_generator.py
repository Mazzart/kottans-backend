"""
Write a password generator in Python.
The passwords should be random, generating a new password every time
the user asks for a new password.

Extra:
Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list
"""

import random
import string

weak = ["test", "123456", "qwerty"]


def pass_generator(size=8,
                   chars=string.ascii_letters
                         + string.digits
                         + string.punctuation) -> str:
    """Returns random password of the specified size"""

    return "".join(random.sample(chars, size))


if __name__ == "__main__":
    pass_strength = input("Choose password option (weak/strong)?: ")
    if pass_strength == "weak":
        print(random.choice(weak))
    else:
        pass_size = int(input("Choose password size: "))
        print(pass_generator(pass_size))
