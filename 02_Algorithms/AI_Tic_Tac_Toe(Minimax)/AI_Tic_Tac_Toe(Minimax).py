"""
🎮 AI Tic-Tac-Toe (Minimax Algorithm)
-------------------------------------
A console-based Tic-Tac-Toe game where you can play against an AI
that uses the Minimax algorithm to make optimal moves.

Author: Abemelek Berhanu
Level: Intermediate - Algorithm & AI

Features:
- Two-player option (Human vs Human)
- Single-player mode with AI (Minimax)
- Board display in the console
- Beginner-friendly and professional code
"""

import math

# Constants for players
HUMAN = "X"
AI = "O"
EMPTY = " "

def create_board():
    """Create an empty 3x3 Tic-Tac-Toe board."""
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Print the board in a user-friendly way."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    """Check if there is a winner. Returns 'X', 'O', or None."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # No winner
    return None

def is_board_full(board):
    """Check if the board is full."""
    for row in board:
        if EMPTY in row:
            return False
    return True

def get_valid_moves(board):
    """Return a list of empty positions on the board."""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move for AI."""
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = AI
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = HUMAN
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    """Determine the best move for AI using Minimax."""
    best_score = -math.inf
    move = None
    for m in get_valid_moves(board):
        board[m[0]][m[1]] = AI
        score = minimax(board, 0, False)
        board[m[0]][m[1]] = EMPTY
        if score > best_score:
            best_score = score
            move = m
    return move

def player_move(board):
    """Handle human player's move input."""
    while True:
        try:
            row = int(input("Enter the row (0,1,2): "))
            col = int(input("Enter the column (0,1,2): "))
            if (row, col) in get_valid_moves(board):
                board[row][col] = HUMAN
                break
            else:
                print("⚠️ Position already taken or invalid. Try again.")
        except ValueError:
            print("⚠️ Please enter valid numbers between 0 and 2.")

def play_game():
    """Main function to play Tic-Tac-Toe."""
    board = create_board()
    print("🎮 Welcome to AI Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'.")
    print_board(board)

    while True:
        # Human turn
        player_move(board)
        print_board(board)
        if check_winner(board) == HUMAN:
            print("🎉 Congratulations! You won!")
            break
        if is_board_full(board):
            print("🤝 It's a tie!")
            break

        # AI turn
        print("🤖 AI is making a move...")
        move = best_move(board)
        board[move[0]][move[1]] = AI
        print_board(board)
        if check_winner(board) == AI:
            print("💻 AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("🤝 It's a tie!")
            break

if __name__ == "__main__":
    play_game()







