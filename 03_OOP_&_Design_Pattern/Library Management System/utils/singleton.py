"""
singleton.py
--------------
Implements the Singleton design pattern.
Ensures that only one Library instance exists in the entire program.
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Return an existing instance or create a new one if it doesn’t exist."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

