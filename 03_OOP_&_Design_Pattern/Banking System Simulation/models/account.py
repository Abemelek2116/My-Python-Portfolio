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
    Represents a savings account with interest accumulation.
    """

    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate  # 2% default annual interest

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

    def apply_interest(self) -> float:
        """
        Apply interest to the current balance.

        :return: Amount of interest added.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


class CheckingAccount(Account):
    """
    Represents a checking account that allows overdrafts up to a limit.
    """

    def __init__(self, account_number: str, owner, balance: float = 0.0, overdraft_limit: float = 500.0):
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
