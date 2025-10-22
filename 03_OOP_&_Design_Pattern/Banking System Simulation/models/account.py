"""
Module: account.py
-------------------
Defines the abstract base class `Account` and its concrete subclasses
`SavingsAccount` and `CheckingAccount`. Demonstrates encapsulation,
inheritance, and polymorphism in an OOP banking simulation.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):
    """
    Abstract base class representing a generic bank account.
    """

    def __init__(self, account_number: str, owner, balance: float = 0.0):
        """
        Initialize a new Account instance.

        :param account_number: Unique identifier for the account
        :param owner: The customer who owns this account
        :param balance: Initial account balance (default 0.0)
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.created_at = datetime.now()

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit a given amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw a given amount from the account."""
        pass

    def __str__(self) -> str:
        """Return a human-readable string representation of the account."""
        return f"{self.__class__.__name__}({self.account_number}) - Owner: {self.owner.name}, Balance: ${self.balance:.2f}"


class SavingsAccount(Account):
    """
    Represents a savings account with standard deposit and withdrawal behavior.
    """

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class CheckingAccount(Account):
    """
    Represents a checking account that allows overdrafts up to a limit.
    """

    def __init__(self, account_number: str, owner, balance: float = 0.0, overdraft_limit: float = 500.0):
        """
        Initialize a checking account with an overdraft limit.

        :param overdraft_limit: The maximum negative balance allowed.
        """
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self.balance -= amount

