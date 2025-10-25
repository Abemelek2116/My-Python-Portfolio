"""
report_service.py
------------------
Generates basic reports for sales and inventory performance.
"""

class ReportService:
    def __init__(self, inventory_service, sale_service):
        self.inventory_service = inventory_service
        self.sale_service = sale_service

    def generate_report(self):
        print("\n=== 🧾 DAILY SALES REPORT ===")
        self.sale_service.show_sales()
        print("\n=== 📦 CURRENT INVENTORY ===")
        self.inventory_service.display_inventory()

