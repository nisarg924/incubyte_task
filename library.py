from book import BookAlreadyBorrowedError, BookExistsError, BookNotBorrowedError, BookNotFoundError


class Library:
    def __init__(self):
        self.books = {}
        
    def add_book(self, book):
        if book.isbn in self.books:
            raise BookExistsError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")
    
    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise BookAlreadyBorrowedError(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        print(f"You have successfully borrowed '{book.title}'.")
    
    def return_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        book = self.books[isbn]
        if not book.is_borrowed:
            raise BookNotBorrowedError(f"The book '{book.title}' was not borrowed.")
        book.is_borrowed = False
        print(f"Thank you for returning '{book.title}'.")
    
    
    def view_available_books(self):
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
        return available_books

def main():
    library = Library()

if __name__ == '__main__':
    main()