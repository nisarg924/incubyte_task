"# Library Management System"
# Library Management System

A simple Library Management System implemented in Python, allowing users to add books, borrow books, return books, and view available books.

## Features

- **Add Books**: Add new books with a unique ISBN, title, author, and publication year.
- **Borrow Books**: Borrow available books. Prevents borrowing if the book is already borrowed.
- **Return Books**: Return borrowed books.
- **View Available Books**: View a list of all available (not borrowed) books.

## Technologies Used

- Python 3.10.7
- `unittest` for testing
- Git for version control

## Setup and Installation

1. **Clone the Repository**:

    ```bash
    git clone <https://github.com/nisarg924/incubyte_task.git>
    ```

2. **Ensure Python is Installed**:

    Make sure you have Python 3.10.7 installed. You can check by running:

    ```bash
    python --version
    ```

3. **Running the Tests**:

    Execute the following command to run all test cases:

    ```bash
    python -m unittest filename.py
    ```

    All tests should pass, indicating that the system functions as expected.

4. **Using the Library Management System**:

    You can interact with the system by importing the `Library` and `Book` classes in a Python script or interpreter.

    **Example Usage**:

    ```python
    from library import Library, Book

    library = Library()

    # Adding books
    book1 = Book("1234567890", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book1)

    # Borrowing a book
    library.borrow_book("1234567890")

    # Viewing available books
    available_books = library.view_available_books()
    for book in available_books:
        print(book)

    # Returning a book
    library.return_book("1234567890")
    ```

## Testing

The project follows Test-Driven Development (TDD) principles. All features are covered by comprehensive test cases . To run the tests, execute:

```bash
python -m unittest filename.py
