# 🧩 Sudoku Solver

A **Python-based Sudoku Solver** that automatically solves any 9x9 Sudoku puzzle using the **backtracking algorithm**.  
This project demonstrates **algorithmic thinking, recursion, and problem-solving skills** in Python.

---

## 🧠 Project Overview

The **Sudoku Solver** program takes a partially filled 9x9 Sudoku grid and fills in the missing numbers to complete the puzzle.  

Key highlights:  
- Automatically solves puzzles of varying difficulty  
- Implements a **backtracking algorithm** to try all possibilities  
- Provides a **clear, readable console output** for the board  
- Beginner-friendly, modular, and professional code

This project helped me practice **recursion, logic validation, and structured problem-solving**.

---

## 🎯 Features

- ✅ Automatically solves any valid 9x9 Sudoku puzzle  
- ✅ Console-based board display with **3x3 box separation**  
- ✅ Backtracking algorithm ensures the **optimal solution**  
- ✅ Beginner-friendly and **well-documented code**  
- ✅ Fully portfolio-ready  

---

## 🧩 How It Works

1. **Find empty cell:** Locate the next empty spot (represented by 0).  
2. **Try numbers 1–9:** For each empty cell, check if a number is valid according to Sudoku rules:  
   - Number must not be in the same row  
   - Number must not be in the same column  
   - Number must not be in the same 3x3 box  
3. **Recursion:** Place the number and recursively attempt to solve the rest of the board.  
4. **Backtrack:** If placing the number leads to no solution, reset the cell to empty and try the next number.  
5. Repeat until the board is completely solved or no solution exists.

---

## 🖥️ Example Run

**Initial Puzzle (0 = empty):**

5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

```markdown

**Solved Puzzle:**

```

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

```yaml

---

## 🛠️ Technologies Used

- **Language:** Python 3  
- **Algorithms:** Backtracking for constraint solving  
- **Tools:** VS Code, PyCharm, Replit  
- **Version Control:** Git & GitHub  

---

## 🧩 Skills Demonstrated

- Recursion and **backtracking algorithms**  
- Logical problem-solving and constraint handling  
- Modular code design for readability and maintenance  
- Debugging and testing algorithm correctness  
- Console-based input/output handling  

---

## 📂 Project Structure
```
sudoku-solver/
│
├── sudoku_solver.py # Main Python source code
└── README.md # Project documentation

```yaml

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/sudoku-solver.git
cd sudoku-solver
```

2.Run the program:
```bash
python sudoku_solver.py
```
3.The program will display the initial puzzle and the solved board in the console.

💼 About Me

Abemelek Berhanu
A passionate Python developer exploring algorithms, AI, and problem-solving projects.
This project demonstrates my dedication to mastering algorithmic thinking and coding fundamentals.

📫 Contact & Profiles

🔗 GitHub: github.com/<your-username>

💼 LinkedIn: linkedin.com/in/<your-linkedin>

📧 Email: your.email@example.com

“Recursion is the heartbeat of problem-solving in programming.”








