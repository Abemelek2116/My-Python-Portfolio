"""
report_service.py
------------------
Generates daily reports for library activities and book status.
"""

class ReportService:
    def __init__(self, library_service, transaction_service):
        self.library_service = library_service
        self.transaction_service = transaction_service

    def generate_report(self):
        print("\n=== 🧾 LIBRARY REPORT ===")
        print(f"Total books: {len(self.library_service.library.books)}")
        print(f"Total members: {len(self.library_service.library.members)}")
        print(f"Total transactions: {len(self.transaction_service.transactions)}")
        print("\nRecent Transactions:")
        for t in self.transaction_service.transactions[-5:]:
            print(t)

