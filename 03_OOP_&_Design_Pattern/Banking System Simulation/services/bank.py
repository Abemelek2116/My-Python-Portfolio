"""
Module: bank.py
---------------
Implements the `Bank` class using the Singleton pattern to ensure
only one bank instance exists during runtime.
"""

from models.account import SavingsAccount, CheckingAccount
from models.customer import Customer
from utils.id_generator import generate_id


class Bank:
    """
    Singleton class representing the bank entity.
    Manages customers and accounts.
    """

    __instance = None  # Private class-level instance variable

    @staticmethod
    def get_instance():
        """
        Static method to get or create the single instance of the Bank.
        """
        if Bank.__instance is None:
            Bank()
        return Bank.__instance

    def __init__(self):
        """
        Initialize the Bank with empty records for customers and accounts.
        Raises an error if multiple instances are created.
        """
        if Bank.__instance is not None:
            raise Exception("Bank is a Singleton class; use Bank.get_instance() instead.")
        self.customers = {}
        self.accounts = {}
        Bank.__instance = self

    def add_customer(self, name: str, email: str) -> Customer:
        """Create and register a new customer in the bank."""
        customer_id = generate_id("CUST")
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_account(self, customer: Customer, account_type: str = "savings"):
        """
        Create a new account for a customer.

        :param customer: Customer object to assign the account to
        :param account_type: 'savings' or 'checking'
        :return: Account object
        """
        acc_number = generate_id("ACC")

        if account_type == "savings":
            account = SavingsAccount(acc_number, customer)
        elif account_type == "checking":
            account = CheckingAccount(acc_number, customer)
        else:
            raise ValueError("Invalid account type specified.")

        customer.add_account(account)
        self.accounts[acc_number] = account
        return account

    def find_account(self, account_number: str):
        """Retrieve an account by its account number."""
        return self.accounts.get(account_number, None)

