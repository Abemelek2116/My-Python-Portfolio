"""
library.py
------------
Central Library class that manages all books and members.
Implements the Singleton pattern.
"""

from utils.singleton import SingletonMeta
from utils.observer import Subject
from models.book import Book
from models.member import Member

class Library(Subject, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        """Add a new book to the collection."""
        book = Book(title, author)
        self.books[book.book_id] = book
        return book

    def register_member(self, name):
        """Register a new library member."""
        member = Member(name)
        self.members[member.member_id] = member
        return member

    def get_book(self, book_id):
        """Return a book by ID."""
        return self.books.get(book_id)

    def get_member(self, member_id):
        """Return a member by ID."""
        return self.members.get(member_id)

