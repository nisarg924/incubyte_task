class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Borrowed: {self.is_borrowed}"

# Errors

class BookExistsError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class BookAlreadyBorrowedError(Exception):
    pass


class BookNotBorrowedError(Exception):
    pass