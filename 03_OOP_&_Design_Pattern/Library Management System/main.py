"""
main.py
--------
Entry point for the Library Management System.
Demonstrates OOP design and pattern implementation.
"""

from services.library_service import LibraryService
from services.transaction_service import TransactionService
from services.report_service import ReportService
from utils.observer import Observer

class NotificationService(Observer):
    """Sends notifications (example: overdue reminders)."""
    def update(self, message):
        print(f"[NOTIFICATION]: {message}")

def main():
    library_service = LibraryService()
    transaction_service = TransactionService()
    report_service = ReportService(library_service, transaction_service)

    # Attach observer to library
    notification_service = NotificationService()
    library_service.library.attach(notification_service)

    # Add books
    book1 = library_service.add_book("1984", "George Orwell")
    book2 = library_service.add_book("To Kill a Mockingbird", "Harper Lee")

    # Register members
    member1 = library_service.register_member("Alice")
    member2 = library_service.register_member("Bob")

    # Borrow and return books
    transaction_service.borrow_book(member1.member_id, book1.book_id)
    transaction_service.borrow_book(member2.member_id, book2.book_id)
    transaction_service.return_book(member1.member_id, book1.book_id)

    # Generate report
    report_service.generate_report()

if __name__ == "__main__":
    main()
