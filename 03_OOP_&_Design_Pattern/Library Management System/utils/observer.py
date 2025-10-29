"""
observer.py
-------------
Implements the Observer design pattern.
Used for sending notifications to members when due dates are reached or other events occur.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Attach an observer (like a notification service)."""
        self._observers.append(observer)

    def notify(self, message):
        """Send a message to all observers."""
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        """Abstract method to handle notifications."""
        raise NotImplementedError

