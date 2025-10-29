"""
member.py
-----------
Represents a library member (borrower).
Keeps track of borrowed books and member info.
"""

from utils.id_generator import IDGenerator

class Member:
    def __init__(self, name):
        self.member_id = IDGenerator.generate_id()
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Add book to borrowed list."""
        self.borrowed_books.append(book)

    def return_book(self, book):
        """Remove book from borrowed list."""
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name} (Borrowed: {len(self.borrowed_books)} books)"

