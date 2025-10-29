"""
id_generator.py
----------------
Generates unique IDs for books, members, and transactions.
"""

import uuid

class IDGenerator:
    @staticmethod
    def generate_id():
        """Generate a short unique ID."""
        return str(uuid.uuid4())[:8]

