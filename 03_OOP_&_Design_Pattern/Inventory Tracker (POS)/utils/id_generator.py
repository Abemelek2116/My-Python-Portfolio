"""
id_generator.py
----------------
Utility class for generating unique IDs for products and sales.
"""

import uuid

class IDGenerator:
    @staticmethod
    def generate_id():
        """Return a unique ID."""
        return str(uuid.uuid4())[:8]

