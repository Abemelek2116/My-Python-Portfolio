"""
🧩 Sudoku Solver
----------------
A Python program to solve any 9x9 Sudoku puzzle using the
backtracking algorithm.

Author: Abemelek Berhanu
Level: Intermediate - Algorithms

Features:
- Solve Sudoku puzzles automatically
- Uses the backtracking algorithm
- Beginner-friendly, modular, and well-commented
- Console-based for easy interaction
"""

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(9):
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += " | "
            row += str(board[i][j]) if board[i][j] != 0 else "."
            row += " "
        print(row)
        if i % 3 == 2 and i != 8:
            print("-" * 21)
    print()

def find_empty(board):
    """Finds an empty spot in the board. Returns (row, col) or None."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    """Checks if placing num at pos is valid according to Sudoku rules."""
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    """Solves the Sudoku board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def main():
    """Main program to run the Sudoku Solver."""
    print("🧩 Welcome to Sudoku Solver!")
    print("Enter the puzzle row by row, use 0 for empty cells.\n")

    # Example puzzle (0 = empty)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("📋 Initial Sudoku Board:")
    print_board(puzzle)

    if solve(puzzle):
        print("✅ Solved Sudoku Board:")
        print_board(puzzle)
    else:
        print("❌ No solution exists for the provided puzzle.")

if __name__ == "__main__":
    main()

