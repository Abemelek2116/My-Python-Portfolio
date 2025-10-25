
"""
observer.py
-------------
Implements the Observer design pattern.
Used for sending notifications (e.g., low stock alerts) when inventory changes.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Attach a new observer."""
        self._observers.append(observer)

    def notify(self, message):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        """Method to be implemented by concrete observers."""
        raise NotImplementedError
