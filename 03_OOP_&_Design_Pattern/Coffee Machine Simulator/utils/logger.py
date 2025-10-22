"""
Module: logger.py
-----------------
Implements an Observer pattern-based logging system.
"""

class Logger:
    """Publisher that notifies subscribers about log events."""

    _subscribers = []

    @classmethod
    def subscribe(cls, observer) -> None:
        cls._subscribers.append(observer)

    @classmethod
    def log(cls, message: str) -> None:
        for sub in cls._subscribers:
            sub.update(message)


class ConsoleLogger:
    """Concrete observer that prints logs to the console."""

    def update(self, message: str) -> None:
        print(f"[LOG]: {message}")

