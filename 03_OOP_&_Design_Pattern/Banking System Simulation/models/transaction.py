"""
Module: transaction.py
----------------------
Defines the `Transaction` class that records fund transfers
between accounts.
"""

from datetime import datetime


class Transaction:
    """
    Represents a money transfer between two accounts.
    """

    def __init__(self, transaction_id: str, from_acc, to_acc, amount: float):
        """
        Initialize a new transaction record.

        :param transaction_id: Unique identifier for the transaction
        :param from_acc: Account object sending funds
        :param to_acc: Account object receiving funds
        :param amount: Amount transferred
        """
        self.transaction_id = transaction_id
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the transaction."""
        return f"[{self.timestamp}] {self.from_acc.account_number} → {self.to_acc.account_number}: ${self.amount:.2f}"

