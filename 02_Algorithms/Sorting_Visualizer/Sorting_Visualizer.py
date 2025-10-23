"""
📊 Sorting Visualizer
---------------------
A Python project that visualizes popular sorting algorithms in real-time.

Author: Abemelek Berhanu
Level: Intermediate - Algorithms & GUI

Features:
- Visualizes Bubble Sort, Insertion Sort, and Selection Sort
- Interactive GUI to start, reset, and choose sorting algorithm
- Beginner-friendly and professional
"""

import tkinter as tk
import random
import time

# GUI constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BAR_WIDTH = 20
BAR_GAP = 5

# Colors
BAR_COLOR = "skyblue"
BAR_COLOR_HIGHLIGHT = "orange"

class SortingVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Sorting Visualizer")

        self.canvas = tk.Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

        self.data = [random.randint(10, 100) for _ in range(20)]
        self.bars = []

        self.draw_bars()

        # Buttons
        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack(pady=10)

        self.bubble_btn = tk.Button(self.btn_frame, text="Bubble Sort", command=self.bubble_sort)
        self.bubble_btn.pack(side=tk.LEFT, padx=5)

        self.insertion_btn = tk.Button(self.btn_frame, text="Insertion Sort", command=self.insertion_sort)
        self.insertion_btn.pack(side=tk.LEFT, padx=5)

        self.selection_btn = tk.Button(self.btn_frame, text="Selection Sort", command=self.selection_sort)
        self.selection_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="Reset", command=self.reset_data)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

    def draw_bars(self, highlight_indices=[]):
        """Draw bars representing the array."""
        self.canvas.delete("all")
        self.bars = []
        x_start = 10
        for i, value in enumerate(self.data):
            x0 = x_start + i * (BAR_WIDTH + BAR_GAP)
            y0 = WINDOW_HEIGHT - value * 3
            x1 = x0 + BAR_WIDTH
            y1 = WINDOW_HEIGHT
            color = BAR_COLOR_HIGHLIGHT if i in highlight_indices else BAR_COLOR
            bar = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.bars.append(bar)
        self.master.update_idletasks()

    def reset_data(self):
        """Reset the array to random values."""
        self.data = [random.randint(10, 100) for _ in range(20)]
        self.draw_bars()

    def bubble_sort(self):
        """Visualize Bubble Sort algorithm."""
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_bars([j, j+1])
                    time.sleep(0.1)

    def insertion_sort(self):
        """Visualize Insertion Sort algorithm."""
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                self.draw_bars([j, j+1])
                time.sleep(0.1)
                j -= 1
            self.data[j + 1] = key
            self.draw_bars([j+1])
            time.sleep(0.1)

    def selection_sort(self):
        """Visualize Selection Sort algorithm."""
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
                self.draw_bars([i, j, min_idx])
                time.sleep(0.1)
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_bars([i, min_idx])
            time.sleep(0.1)

def main():
    root = tk.Tk()
    SortingVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

