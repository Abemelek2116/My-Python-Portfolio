"""
Module: id_generator.py
-----------------------
Provides utility function for generating unique order or transaction IDs.
"""

import random, string

def generate_id(prefix: str) -> str:
    """Generate a unique alphanumeric ID."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{code}"

