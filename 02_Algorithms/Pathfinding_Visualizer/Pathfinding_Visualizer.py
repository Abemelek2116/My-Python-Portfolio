"""
📍 Pathfinding Visualizer (A* Algorithm)
---------------------------------------
A simple Python project that visualizes the A* pathfinding algorithm
on a grid. The program finds the shortest path from a start node
to an end node while avoiding obstacles.

Author: Abemelek Berhanu
Level: Intermediate - Algorithms & AI

Features:
- Grid-based pathfinding visualization
- Supports user-defined start, end, and obstacles
- Implements A* algorithm for optimal path finding
- Beginner-friendly and professional code
"""

import tkinter as tk
from queue import PriorityQueue

# Grid parameters
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Colors
EMPTY_COLOR = "white"
START_COLOR = "green"
END_COLOR = "red"
OBSTACLE_COLOR = "black"
PATH_COLOR = "yellow"
OPEN_COLOR = "blue"
CLOSED_COLOR = "grey"

class Cell:
    """Represents each cell in the grid."""
    def __init__(self, row, col, canvas):
        self.row = row
        self.col = col
        self.canvas = canvas
        self.is_obstacle = False
        self.is_start = False
        self.is_end = False
        self.rect = canvas.create_rectangle(
            col*CELL_SIZE, row*CELL_SIZE,
            (col+1)*CELL_SIZE, (row+1)*CELL_SIZE,
            fill=EMPTY_COLOR, outline="black"
        )

    def set_color(self, color):
        self.canvas.itemconfig(self.rect, fill=color)

def heuristic(a, b):
    """Heuristic function for A* (Manhattan distance)."""
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(grid, start, end, canvas):
    """A* pathfinding algorithm implementation."""
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = heuristic((start.row, start.col), (end.row, end.col))
    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # reconstruct path
            while current in came_from:
                current = came_from[current]
                if current != start:
                    current.set_color(PATH_COLOR)
            return True

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic((neighbor.row, neighbor.col), (end.row, end.col))
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end:
                        neighbor.set_color(OPEN_COLOR)
        if current != start:
            current.set_color(CLOSED_COLOR)
        canvas.update()

    return False

def get_neighbors(grid, cell):
    """Return walkable neighbors of a cell."""
    neighbors = []
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in dirs:
        r, c = cell.row + dx, cell.col + dy
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            neighbor = grid[r][c]
            if not neighbor.is_obstacle:
                neighbors.append(neighbor)
    return neighbors

def main():
    """Main function to create GUI and run pathfinding visualizer."""
    root = tk.Tk()
    root.title("Pathfinding Visualizer - A* Algorithm")

    canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE)
    canvas.pack()

    # Create grid
    grid = [[Cell(r, c, canvas) for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]

    start = None
    end = None

    def click(event):
        nonlocal start, end
        row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
        cell = grid[row][col]
        if not start:
            start = cell
            cell.is_start = True
            cell.set_color(START_COLOR)
        elif not end and cell != start:
            end = cell
            cell.is_end = True
            cell.set_color(END_COLOR)
        elif cell != start and cell != end:
            cell.is_obstacle = not cell.is_obstacle
            cell.set_color(OBSTACLE_COLOR if cell.is_obstacle else EMPTY_COLOR)

    canvas.bind("<Button-1>", click)

    def start_algorithm():
        if start and end:
            a_star(grid, start, end, canvas)

    btn = tk.Button(root, text="Start A* Pathfinding", command=start_algorithm)
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

