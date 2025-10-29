"""
book.py
--------
Represents a single book in the library system.
Encapsulates details such as title, author, and availability status.
"""

from utils.id_generator import IDGenerator

class Book:
    def __init__(self, title, author):
        self.book_id = IDGenerator.generate_id()
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        """Mark book as borrowed."""
        if not self.available:
            raise ValueError("Book is currently unavailable.")
        self.available = False

    def return_book(self):
        """Mark book as available again."""
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"

