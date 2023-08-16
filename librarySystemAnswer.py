class Library:
    def __init__(self):
        self.books = []

    def addBook(self, bookName):
        self.books.append(bookName)

# Removed inheritance from Book and Member classes

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    # ... (other methods remain unchanged)

class Member:  
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []

    def borrow(self, book):
        if book.available:
            book.borrowBook()
            self.borrowedBooks.append(book)
        else:
            print(f"Sorry, {book.title} is unavailable")

lib1 = Library()  # Removed the unnecessary method call
lib2 = Library()  # Removed the unnecessary method call
lib3 = Library()  # Removed the unnecessary method call

lib1.addBook("Test Book")  # Added books to libraries using addBook method
lib2.addBook("Another book")  # Added books to libraries using addBook method
lib3.addBook("Big book")  # Added books to libraries using addBook method

book1 = Book("Test Book", "Suf")
book2 = Book("Another book", "Elz")
book3 = Book("Big book", "Hay")

mem1 = Member("Sufyaan")
mem1.borrow(book2)
