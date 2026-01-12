#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        # columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row = int(input("Row (0-2): "))
        col = int(input("Col (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position!")
            continue

        if board[row][col] != " ":
            print("Spot taken!")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player", player, "wins!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
