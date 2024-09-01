import unittest

from book import Book, BookAlreadyBorrowedError, BookNotFoundError
from library import Library


class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("978-3-16-148410-0", " Samrat Ashoka", "Ancestor", 1925)
        self.book2 = Book("978-3-16-148411-0", "Ramayan", "Valmiki", 1949)
        self.book3 = Book("978-3-16-148412-0", "Mahabharat", "Vedvyas", 1960)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        
    def test_borrow_book_success(self):
        self.library.borrow_book(self.book1.isbn)
        self.assertTrue(self.library.books[self.book1.isbn].is_borrowed)


    def test_borrow_book_not_found(self):
        with self.assertRaises(BookNotFoundError) as context:
            self.library.borrow_book("0000000000")
        self.assertEqual(str(context.exception), "No book found with ISBN 0000000000.")


    def test_borrow_book_already_borrowed(self):
        self.library.borrow_book(self.book1.isbn)
        with self.assertRaises(BookAlreadyBorrowedError) as context:
            self.library.borrow_book(self.book1.isbn)
        self.assertEqual(str(context.exception), f"The book '{self.book1.title}' is already borrowed.")