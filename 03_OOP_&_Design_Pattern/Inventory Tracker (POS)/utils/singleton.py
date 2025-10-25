
"""
singleton.py
--------------
Implements the Singleton design pattern.
Used to ensure classes like Inventory have only one instance throughout the app.
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Return existing instance if present, else create one."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
