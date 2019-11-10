"""
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user,
will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out
how many guesses it took to get your number.
"""


def guessing_game(n):
    min, max = 0, 100
    computer_guess = (min + max) // 2
    guesses = 1
    while n != computer_guess:
        print(f"Computer guess is: {computer_guess}")
        your_number = input("Is your number lower or higher? ")
        if your_number == "lower":
            max = computer_guess
        elif your_number == 'higher':
            min = computer_guess
        computer_guess = (min + max) // 2
        guesses += 1

    print(f"Your number is {computer_guess} and it took {guesses} guesses.")


if __name__ == "__main__":
    n = int(input("Enter your number from 0 to 100: "))
    guessing_game(n)
