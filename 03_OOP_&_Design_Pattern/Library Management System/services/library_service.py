"""
library_service.py
-------------------
Provides an interface for managing books and members in the library.
"""

from models.library import Library

class LibraryService:
    def __init__(self):
        self.library = Library()

    def add_book(self, title, author):
        book = self.library.add_book(title, author)
        print(f"✅ Added book: {book}")
        return book

    def register_member(self, name):
        member = self.library.register_member(name)
        print(f"✅ Registered member: {member}")
        return member

    def show_books(self):
        print("\n=== 📚 Library Collection ===")
        for book in self.library.books.values():
            print(book)

    def show_members(self):
        print("\n=== 👥 Library Members ===")
        for member in self.library.members.values():
            print(member)

