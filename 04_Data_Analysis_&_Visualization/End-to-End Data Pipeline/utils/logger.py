"""
logger.py
---------
Simple timestamped logger for consistent messaging across the pipeline.
"""

from datetime import datetime

class Logger:
    """Utility class for logging messages with timestamps."""

    @staticmethod
    def log(message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

