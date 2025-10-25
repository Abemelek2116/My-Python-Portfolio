"""
inventory.py
-------------
Maintains a list of products.
Implements Singleton (only one inventory in the system).
Uses Observer to notify low stock events.
"""

from utils.singleton import SingletonMeta
from utils.observer import Subject
from models.product import Product

class Inventory(Subject, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.products = {}

    def add_product(self, name, price, quantity):
        """Add a new product to the inventory."""
        product = Product(name, price, quantity)
        self.products[product.product_id] = product
        return product

    def remove_product(self, product_id):
        """Remove a product from the inventory."""
        if product_id in self.products:
            del self.products[product_id]

    def get_product(self, product_id):
        """Return product by ID."""
        return self.products.get(product_id)

    def list_products(self):
        """Return a list of all products."""
        return list(self.products.values())

    def update_stock(self, product_id, amount):
        """Update product quantity and trigger low stock notification."""
        product = self.get_product(product_id)
        if product:
            product.reduce_stock(amount)
            if product.quantity < 3:
                self.notify(f"⚠️ Low stock alert: {product.name} (Remaining: {product.quantity})")

