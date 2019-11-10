"""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have
a “cow”. For every digit the user guessed correctly in the wrong place is
a “bull”. Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number,
the game is over. Keep track of the number of guesses the user makes throughout
the game and tell the user at the end.
"""
import random


def game_start():
    print("Welcome to the Cows and Bulls Game!")
    print("Enter a 4-digit number:")
    n = input("")
    return n


def cows_bulls(n, r):
    cows, bulls = 0, 0
    for i in range(4):
        if n[i] == r[i]:
            cows += 1
        elif n[i] in r:
            bulls += 1

    return cows, bulls


if __name__ == "__main__":
    r = str(random.randint(1000, 9999))
    cows, bulls = cows_bulls(game_start(), r)
    guesses = 0
    while cows != 4:
        guesses += 1
        print(f"{cows} cows, {bulls} bulls")
        cows, bulls = cows_bulls(game_start(), r)
    print(f"You won. Number of guesses is: {guesses}")
