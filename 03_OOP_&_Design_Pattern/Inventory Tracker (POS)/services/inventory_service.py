"""
inventory_service.py
---------------------
Provides high-level methods for managing inventory operations.
"""

from models.inventory import Inventory

class InventoryService:
    def __init__(self):
        self.inventory = Inventory()

    def add_new_product(self, name, price, quantity):
        return self.inventory.add_product(name, price, quantity)

    def display_inventory(self):
        for product in self.inventory.list_products():
            print(product)

