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
import random
import time

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


# === STEP 1: Helper boards and game utilities ===
def get_random_board(level):
    """Return a puzzle (9x9 list) for the requested difficulty level (1-7).
    A few example puzzles are hardcoded for each level. The function returns
    a deep copy so callers can modify the returned board safely.
    """
    # Each level maps to a list of candidate puzzles; pick one at random.
    # 0 represents an empty cell. Puzzles chosen to be solvable by the solver.
    boards = {
        1: [
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ],
        ],
        2: [
            [
                [0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0],
            ],
        ],
        3: [
            [
                [0, 2, 0, 6, 0, 8, 0, 0, 0],
                [5, 8, 0, 0, 0, 9, 7, 0, 0],
                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                [3, 7, 0, 0, 0, 0, 5, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 8, 0, 0, 0, 0, 1, 3],
                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 0, 9, 8, 0, 0, 0, 3, 6],
                [0, 0, 0, 3, 0, 6, 0, 9, 0],
            ],
        ],
        4: [
            [
                [0, 0, 0, 0, 0, 7, 0, 9, 0],
                [1, 0, 0, 0, 6, 0, 0, 0, 0],
                [0, 0, 0, 4, 0, 0, 2, 0, 0],
                [0, 0, 5, 0, 0, 0, 0, 7, 3],
                [0, 0, 2, 0, 0, 0, 6, 0, 0],
                [9, 7, 0, 0, 0, 0, 5, 0, 0],
                [0, 0, 6, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 5, 0, 0, 0, 9],
                [0, 4, 0, 2, 0, 0, 0, 0, 0],
            ],
        ],
        5: [
            [
                [0, 0, 0, 6, 0, 0, 4, 0, 0],
                [7, 0, 0, 0, 0, 3, 6, 0, 0],
                [0, 0, 0, 0, 9, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 0, 1, 8, 0, 0, 0, 3],
                [0, 0, 0, 3, 0, 6, 0, 4, 5],
                [0, 4, 0, 2, 0, 0, 0, 6, 0],
                [9, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 1, 0, 0],
            ],
        ],
        6: [
            [
                [0, 0, 0, 0, 0, 0, 8, 0, 0],
                [0, 0, 0, 0, 7, 3, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 0, 0, 0, 2, 0],
                [0, 0, 0, 5, 0, 1, 0, 0, 0],
                [0, 3, 0, 0, 0, 0, 0, 6, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 9, 8, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0, 0],
            ],
        ],
        7: [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        ],
    }

    candidates = boards.get(max(1, min(7, level)), boards[1])
    # return a deep copy so caller can modify
    chosen = random.choice(candidates)
    return [row[:] for row in chosen]


def print_board_with_coords(board):
    """Print board with row/column indices and '.' for empty cells."""
    print("    " + " ".join(str(i+1) for i in range(9)))
    for i in range(9):
        row_str = f"{i+1:2}  "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(board[i][j]) if board[i][j] != 0 else ".") + " "
        print(row_str)
        if i % 3 == 2 and i != 8:
            print("   " + "- " * 11)
    print()


# === STEP 2: User interaction loop ===
def user_play(start_board):
    """Let the user fill in missing cells one-by-one. Returns the user's board and elapsed time."""
    # Make copies: user's board (what they fill) and solved board (reference)
    user_board = [row[:] for row in start_board]
    solved_board = [row[:] for row in start_board]
    if not solve(solved_board):
        # If the provided puzzle isn't solvable, return immediately
        print("Provided puzzle has no valid solution. Cannot start game.")
        return user_board, 0.0

    # Gather list of empty positions in a stable order (row-major)
    empty_positions = [(r, c) for r in range(9) for c in range(9) if start_board[r][c] == 0]

    print("🧩 Let's begin! Fill the missing numbers. Type 'skip' to move on to the next cell.")
    start_time = time.time()

    for idx, (r, c) in enumerate(empty_positions, start=1):
        while True:
            print(f"\nCell {idx}/{len(empty_positions)} -> row {r+1}, col {c+1}")
            print_board_with_coords(user_board)
            ans = input("Enter a number (1-9) for this cell, or 'skip' to leave it empty: ").strip().lower()
            if ans == 'skip':
                print("Skipped. Moving on.")
                break
            # Allow quitting early
            if ans in ('q', 'quit', 'exit'):
                print("Exiting the round early.")
                elapsed = time.time() - start_time
                return user_board, elapsed
            # Validate numeric input
            if not ans.isdigit() or not (1 <= int(ans) <= 9):
                print("Please enter a digit 1-9, or type 'skip'.")
                continue
            num = int(ans)
            # Check against solved board
            if num == solved_board[r][c]:
                user_board[r][c] = num
                print("✅ Correct!")
                break
            else:
                print("❌ Wrong! Try again or type 'skip' to move on.")
                # do not modify user_board on wrong answer
                continue

    elapsed = time.time() - start_time
    return user_board, elapsed


# === STEP 3: Game start and flow ===
def start_game():
    """Interactive entry for the Sudoku Trainer game."""
    print("🧩 Welcome to Sudoku Trainer!")
    print("Choose difficulty level (1 - easiest, 7 - hardest). Enter a number between 1 and 7.")

    # Ask user for level
    while True:
        level_input = input("Select level (1-7): ").strip()
        if level_input.isdigit() and 1 <= int(level_input) <= 7:
            level = int(level_input)
            break
        print("Please enter an integer from 1 to 7.")

    # Get puzzle for level
    puzzle = get_random_board(level)

    print("\n📋 Initial Sudoku Board:")
    print_board_with_coords(puzzle)

    # Let the user play (fill missing cells)
    user_board, elapsed = user_play(puzzle)

    # When user finishes show results
    print(f"\n⏱ Time taken: {elapsed:.1f} seconds")

    print("\n🧾 Your final board:")
    print_board_with_coords(user_board)

    # Show solved board for comparison
    solved = [row[:] for row in puzzle]
    if solve(solved):
        print("✅ Solved board:")
        print_board_with_coords(solved)
    else:
        print("(Note) Could not compute solved board to compare.")


if __name__ == "__main__":
    start_game()

