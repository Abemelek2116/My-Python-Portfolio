"""
Module: transaction_service.py
------------------------------
Implements a transaction management service following the
Strategy pattern to handle money transfers between accounts.
"""

from models.transaction import Transaction
from utils.id_generator import generate_id


class TransactionService:
    """
    Handles all money transfer operations and records transaction history.
    """

    def __init__(self):
        """Initialize the service with an empty transaction log."""
        self.transactions = []

    def transfer(self, from_acc, to_acc, amount: float) -> Transaction:
        """
        Execute a money transfer between two accounts.

        :param from_acc: Source account object
        :param to_acc: Destination account object
        :param amount: Amount to transfer
        :return: Transaction object representing the operation
        """
        if from_acc == to_acc:
            raise ValueError("Cannot transfer to the same account.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        # Perform fund movement
        from_acc.withdraw(amount)
        to_acc.deposit(amount)

        # Record transaction
        transaction = Transaction(generate_id("TXN"), from_acc, to_acc, amount)
        self.transactions.append(transaction)
        return transaction

    def get_history(self):
        """Return a list of all completed transactions."""
        return self.transactions

