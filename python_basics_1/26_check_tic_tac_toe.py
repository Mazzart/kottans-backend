"""
Given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don't worry about the case where TWO people have won -
assume that in every board there will only be one winner.
"""

winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]


def tic_tac_toe(board):
    for i in range(3):
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != 0:
            return board[i][0]

    for i in range(3):
        column = set([board[0][i], board[1][i], board[2][i]])
        if len(column) == 1 and board[0][i] != 0:
            return board[0][i]

    diagonal_1 = set([board[0][0], board[1][1], board[2][2]])
    diagonal_2 = set([board[-1][0], board[1][1], board[0][-1]])
    if len(diagonal_1) == 1 or len(diagonal_2) == 1 and board[1][1] != 0:
        return board[1][1]

    return 0


if __name__ == "__main__":
    for board in [winner_is_2, winner_is_1, winner_is_also_1,
                  no_winner, also_no_winner]:
        result = tic_tac_toe(board)
        if result == 0:
            print("No winner")
        else:
            print(f"Winner is {result}")
