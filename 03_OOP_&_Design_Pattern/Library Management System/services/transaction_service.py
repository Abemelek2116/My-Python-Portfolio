"""
transaction_service.py
-----------------------
Handles borrowing and returning transactions between members and books.
"""

from models.transaction import Transaction
from models.library import Library

class TransactionService:
    def __init__(self):
        self.library = Library()
        self.transactions = []

    def borrow_book(self, member_id, book_id):
        member = self.library.get_member(member_id)
        book = self.library.get_book(book_id)
        if not (member and book):
            print("❌ Invalid member or book ID.")
            return
        if not book.available:
            print("⚠️ Book already borrowed.")
            return

        book.borrow()
        member.borrow_book(book)
        transaction = Transaction(member, book, "borrow")
        self.transactions.append(transaction)
        print(f"✅ {member.name} borrowed '{book.title}'")

    def return_book(self, member_id, book_id):
        member = self.library.get_member(member_id)
        book = self.library.get_book(book_id)
        if not (member and book):
            print("❌ Invalid member or book ID.")
            return

        book.return_book()
        member.return_book(book)
        transaction = Transaction(member, book, "return")
        self.transactions.append(transaction)
        print(f"✅ {member.name} returned '{book.title}'")

