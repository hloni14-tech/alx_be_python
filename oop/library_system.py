class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author must be provided")
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        if file_size is None or file_size < 0:
            raise ValueError("File size must be a non-negative integer")
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        if page_count is None or page_count <= 0:
            raise ValueError("Page count must be a positive integer")
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book or its subclasses can be added")
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(str(book))