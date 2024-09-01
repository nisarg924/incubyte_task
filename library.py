from book import BookExistsError


class Library:
    def __init__(self):
        self.books = {}
        
        def add_book(self, book):
            if book.isbn in self.books:
                raise BookExistsError(f"Book with ISBN {book.isbn} already exists.")
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added successfully.")
        
def main():
    library = Library()

if __name__ == '__main__':
    main()