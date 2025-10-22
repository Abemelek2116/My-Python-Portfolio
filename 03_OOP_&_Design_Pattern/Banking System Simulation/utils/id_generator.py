"""
Module: id_generator.py
-----------------------
Provides utility function to generate unique IDs for
customers, accounts, and transactions.
"""

import random
import string


def generate_id(prefix: str) -> str:
    """
    Generate a unique alphanumeric ID with a given prefix.

    :param prefix: The type prefix (e.g., 'ACC', 'CUST', 'TXN')
    :return: Unique string ID
    """
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{random_part}"

