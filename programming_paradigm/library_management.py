from book import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        self._books.append(Book(title, author))

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        for book in available:
            print(f"Title: {book.title}, Author: {book.author}")
        if not available:
            print("No available books.")
