import unittest

from book import Book
from library import BookExistsError, Library


class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("978-3-16-148410-0", " Samrat Ashoka", "Ancestor", 1925)
        self.book2 = Book("978-3-16-148411-0", "Ramayan", "Valmiki", 1949)
        self.book3 = Book("978-3-16-148412-0", "Mahabharat", "Vedvyas", 1960)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book_success(self):
        self.library.add_book(self.book3)
        self.assertIn(self.book3.isbn, self.library.books)
        self.assertEqual(self.library.books[self.book3.isbn], self.book3)


    def test_add_book_duplicate_isbn(self):
        with self.assertRaises(BookExistsError) as context:
            duplicate_book = Book("978-3-16-148410-0", "Duplicate Book", "Author", 2000)
            self.library.add_book(duplicate_book)
        self.assertEqual(str(context.exception), "Book with ISBN 978-3-16-148410-0 already exists.")