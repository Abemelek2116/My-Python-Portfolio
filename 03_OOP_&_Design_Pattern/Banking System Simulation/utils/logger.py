"""
Module: logger.py
-----------------
Implements a simple Observer pattern-based logging system.
Allows multiple subscribers to receive event notifications.
"""

class Logger:
    """
    Publisher class that notifies all subscribed observers
    when a new log message is available.
    """

    _subscribers = []

    @classmethod
    def subscribe(cls, observer) -> None:
        """Subscribe an observer to receive log updates."""
        cls._subscribers.append(observer)

    @classmethod
    def log(cls, message: str) -> None:
        """Notify all observers with a log message."""
        for sub in cls._subscribers:
            sub.update(message)


class ConsoleLogger:
    """
    Concrete observer that prints log messages to the console.
    """

    def update(self, message: str) -> None:
        """Handle log message updates."""
        print(f"[LOG]: {message}")

