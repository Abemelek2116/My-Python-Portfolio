"""
utils.py
--------
Utility functions for logging and saving files.
"""

from datetime import datetime
import os

def log(message: str):
    """Logs timestamped messages for consistent tracking."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def ensure_dir(directory: str):
    """Ensures the given directory exists."""
    os.makedirs(directory, exist_ok=True)

