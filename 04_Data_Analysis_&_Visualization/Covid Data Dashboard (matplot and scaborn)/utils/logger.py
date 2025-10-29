"""
logger.py
---------
Simple static logger to provide consistent status messages across modules.
"""

from datetime import datetime


class Logger:
    """Utility logger class for printing timestamped messages."""

    @staticmethod
    def log(message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

