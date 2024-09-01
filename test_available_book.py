import unittest

from book import Book
from library import Library


class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("978-3-16-148410-0", " Samrat Ashoka", "Ancestor", 1925)
        self.book2 = Book("978-3-16-148411-0", "Ramayan", "Valmiki", 1949)
        self.book3 = Book("978-3-16-148412-0", "Mahabharat", "Vedvyas", 1960)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
    
    def test_view_available_books_all_available(self):
        available_books = self.library.view_available_books()
        self.assertIn(self.book1, available_books)
        self.assertIn(self.book2, available_books)
        self.assertEqual(len(available_books), 2)

    def test_view_available_books_some_borrowed(self):
        self.library.borrow_book(self.book1.isbn)
        available_books = self.library.view_available_books()
        self.assertNotIn(self.book1, available_books)
        self.assertIn(self.book2, available_books)
        self.assertEqual(len(available_books), 1)

    def test_view_available_books_none_available(self):
        self.library.borrow_book(self.book1.isbn)
        self.library.borrow_book(self.book2.isbn)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 0)