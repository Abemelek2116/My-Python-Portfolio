"""
id_generator.py
----------------
Simple, deterministic ID generation for plugins and other objects.
"""

import uuid


class IDGenerator:
    @staticmethod
    def generate_id() -> str:
        """Return a short unique id suitable for registry keys."""
        return str(uuid.uuid4())[:8]
