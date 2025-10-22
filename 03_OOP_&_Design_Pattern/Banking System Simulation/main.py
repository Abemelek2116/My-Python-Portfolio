"""
Main Script: Banking System Simulation
--------------------------------------
Entry point for running the banking system simulation.
Demonstrates the use of OOP and multiple design patterns.
"""

from services.bank import Bank
from services.transaction_service import TransactionService
from utils.logger import Logger, ConsoleLogger


def main():
    """
    Main function that runs the simulation.
    """
    # Attach a console logger to observe real-time system events
    Logger.subscribe(ConsoleLogger())

    # Create bank instance (Singleton)
    bank = Bank.get_instance()
    tx_service = TransactionService()

    # Register customers
    alice = bank.add_customer("Alice Johnson", "alice@example.com")
    bob = bank.add_customer("Bob Smith", "bob@example.com")

    # Create accounts for customers
    alice_acc = bank.create_account(alice, "savings")
    bob_acc = bank.create_account(bob, "checking")

    # Perform operations
    alice_acc.deposit(1000)
    Logger.log(f"{alice.name} deposited $1000.")

    # Execute a fund transfer
    transaction = tx_service.transfer(alice_acc, bob_acc, 200)
    Logger.log(f"Transaction completed: {transaction}")

    # Display final balances
    print("\n=== Final Balances ===")
    print(alice_acc)
    print(bob_acc)


if __name__ == "__main__":
    main()

