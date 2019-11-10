"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order.
"""

user_message = input("Enter your message: ")

def string_reverse(words: str) -> str:
    """Returns the given words in reverse order"""

    result = words.split()
    return " ".join(result[::-1])


if __name__ == "__main__":
    print(string_reverse(user_message))
