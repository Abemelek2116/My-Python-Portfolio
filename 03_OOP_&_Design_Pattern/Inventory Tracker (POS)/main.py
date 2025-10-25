"""
main.py
--------
Entry point for the Inventory Tracker POS System.
Demonstrates interaction between modules, OOP design, and patterns.
"""

from services.inventory_service import InventoryService
from services.sale_service import SaleService
from services.report_service import ReportService
from utils.observer import Observer

class NotificationService(Observer):
    """Receives notifications about low stock and displays them."""
    def update(self, message):
        print(f"[NOTIFICATION]: {message}")

def main():
    inventory_service = InventoryService()
    sale_service = SaleService()
    report_service = ReportService(inventory_service, sale_service)

    # Attach observer to inventory
    notification_service = NotificationService()
    inventory_service.inventory.attach(notification_service)

    # Add products
    coffee = inventory_service.add_new_product("Coffee", 5.0, 10)
    tea = inventory_service.add_new_product("Tea", 3.5, 2)
    milk = inventory_service.add_new_product("Milk", 2.0, 5)

    # Make some sales
    sale_service.process_sale(coffee.product_id, 3)
    sale_service.process_sale(tea.product_id, 1)
    sale_service.process_sale(milk.product_id, 3)

    # Generate report
    report_service.generate_report()

if __name__ == "__main__":
    main()

