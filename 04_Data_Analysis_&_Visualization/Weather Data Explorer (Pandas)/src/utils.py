"""
utils.py
--------
Utility functions for logging and directory management.
"""

from datetime import datetime
import os


def log(message: str):
    """Logs timestamped messages to the console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def ensure_dir(directory: str):
    """Ensures that the given directory exists."""
    os.makedirs(directory, exist_ok=True)

