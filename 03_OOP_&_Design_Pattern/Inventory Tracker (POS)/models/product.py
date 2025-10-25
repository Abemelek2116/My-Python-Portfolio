"""
product.py
-----------
Represents a single product in the inventory.
Encapsulates product data and methods to adjust stock.
"""

from utils.id_generator import IDGenerator

class Product:
    def __init__(self, name, price, quantity):
        self.product_id = IDGenerator.generate_id()
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_stock(self, amount):
        """Reduce stock after a sale."""
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount

    def __str__(self):
        return f"{self.name} (${self.price}) — Stock: {self.quantity}"

