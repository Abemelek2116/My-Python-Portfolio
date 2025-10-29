"""
transaction.py
----------------
Represents a borrowing or returning transaction in the system.
"""

from datetime import datetime, timedelta
from utils.id_generator import IDGenerator

class Transaction:
    def __init__(self, member, book, transaction_type):
        self.transaction_id = IDGenerator.generate_id()
        self.member = member
        self.book = book
        self.transaction_type = transaction_type
        self.date = datetime.now()
        self.due_date = self.date + timedelta(days=7) if transaction_type == "borrow" else None

    def __str__(self):
        return f"Transaction #{self.transaction_id}: {self.member.name} {self.transaction_type}ed '{self.book.title}' on {self.date.strftime('%Y-%m-%d')}"

