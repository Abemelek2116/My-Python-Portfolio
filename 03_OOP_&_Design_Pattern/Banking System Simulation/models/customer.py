"""
Module: customer.py
-------------------
Defines the `Customer` class, representing a bank client
who may hold multiple accounts.
"""

class Customer:
    """
    Represents a customer of the bank.
    """

    def __init__(self, customer_id: str, name: str, email: str):
        """
        Initialize a customer profile.

        :param customer_id: Unique ID assigned to the customer
        :param name: Customer's full name
        :param email: Customer's email address
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account) -> None:
        """Link an account to this customer."""
        self.accounts.append(account)

    def get_total_balance(self) -> float:
        """Compute the total balance across all accounts owned by the customer."""
        return sum(acc.balance for acc in self.accounts)

    def __str__(self) -> str:
        """Return a readable representation of the customer."""
        return f"Customer({self.name}, Email: {self.email})"

