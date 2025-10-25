"""
sale.py
--------
Represents a single sale transaction.
"""

from utils.id_generator import IDGenerator

class Sale:
    def __init__(self, product, quantity):
        self.sale_id = IDGenerator.generate_id()
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Sale #{self.sale_id}: {self.product.name} x {self.quantity} = ${self.total_price:.2f}"

