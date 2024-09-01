from book import Book, BookAlreadyBorrowedError, BookExistsError, BookNotBorrowedError, BookNotFoundError


class Library:
    def __init__(self):
        self.books = {}
    
    #add book feature
    
    def add_book(self, book):
        if book.isbn in self.books:
            raise BookExistsError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")
    
    #borrow book feature
    
    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise BookAlreadyBorrowedError(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        print(f"You have successfully borrowed '{book.title}'.")
    
    #return book feature
    
    def return_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        book = self.books[isbn]
        if not book.is_borrowed:
            raise BookNotBorrowedError(f"The book '{book.title}' was not borrowed.")
        book.is_borrowed = False
        print(f"Thank you for returning '{book.title}'.")
    
    #view availble book feature
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
    
    #for user input
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")

            try:
                book = Book(isbn, title, author, int(year))
                library.add_book(book)
            except BookExistsError as e:
                print(e)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to borrow: ")

            try:
                library.borrow_book(isbn)
            except (BookNotFoundError, BookAlreadyBorrowedError) as e:
                print(e)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")

            try:
                library.return_book(isbn)
            except (BookNotFoundError, BookNotBorrowedError) as e:
                print(e)

        elif choice == '4':
            library.view_available_books()

        elif choice == '5':
            print("Nice to have you in coding!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()