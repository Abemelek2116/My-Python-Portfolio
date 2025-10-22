"""
Module: file_handler.py
-----------------------
Provides functionality to export order history to a CSV file.
"""

import csv

def export_orders_to_csv(orders, filename="orders.csv") -> None:
    """Export all completed drink orders to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Drink", "Price"])
        for order in orders:
            writer.writerow([order.name, f"{order.price:.2f}"])

