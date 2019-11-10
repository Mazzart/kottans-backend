"""
Ask the user what size game board they want to draw,
and draw it for them to the screen using Python’s print statement.
"""


def create_board(board_size):
    for i in range(board_size):
        print(" ---" * board_size)
        print("|   " * (board_size + 1))
    print(" ---" * board_size)


if __name__ == "__main__":
    board_size = int(input("Enter game board size: "))
    create_board(board_size)
