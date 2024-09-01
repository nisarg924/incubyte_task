from book import BookAlreadyBorrowedError, BookExistsError, BookNotFoundError


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
    
def main():
    library = Library()

if __name__ == '__main__':
    main()