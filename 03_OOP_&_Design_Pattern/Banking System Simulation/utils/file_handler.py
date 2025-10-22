"""
Module: file_handler.py
-----------------------
Provides utility functions for exporting transaction history to CSV.
"""

import csv
from models.transaction import Transaction


def export_transactions_to_csv(transactions: list[Transaction], filename: str = "transactions.csv") -> None:
    """
    Export a list of Transaction objects to a CSV file.

    :param transactions: List of Transaction objects
    :param filename: CSV output file name
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction ID", "From Account", "To Account", "Amount", "Timestamp"])
        for txn in transactions:
            writer.writerow([
                txn.transaction_id,
                txn.from_acc.account_number,
                txn.to_acc.account_number,
                f"{txn.amount:.2f}",
                txn.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            ])

