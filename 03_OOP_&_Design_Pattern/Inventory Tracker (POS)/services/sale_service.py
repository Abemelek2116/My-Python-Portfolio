"""
sale_service.py
----------------
Handles the business logic for processing sales.
"""

from models.sale import Sale
from models.inventory import Inventory

class SaleService:
    def __init__(self):
        self.inventory = Inventory()
        self.sales = []

    def process_sale(self, product_id, quantity):
        product = self.inventory.get_product(product_id)
        if not product:
            print("Product not found.")
            return
        sale = Sale(product, quantity)
        product.reduce_stock(quantity)
        self.sales.append(sale)
        print(f"✅ Sale completed: {sale}")
        if product.quantity < 3:
            self.inventory.notify(f"⚠️ Low stock alert: {product.name} (Remaining: {product.quantity})")

    def show_sales(self):
        for sale in self.sales:
            print(sale)

