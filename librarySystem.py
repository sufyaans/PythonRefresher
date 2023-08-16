'''
Design a library system with classes like Library, Book, and Member. 
The Library class should manage books and members, while the Book class should have attributes like title, author, and availability. 
The Member class can have attributes like name and borrowed books.
'''

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, bookName):
        self.books.append(bookName)
        return bookName
        

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkBook(self):
        if self.available == True:
            print(f"{self.title} is available to borrow")
        else:
            print(f"{self.available} is unavailable")


    def borrowBook(self):
        if self.available:
            self.available = False
            print(f"You have borrowed {self.title}.")
        else:
            print(f"Sorry {self.title} has already been borrowed")



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


lib1 = Library()
lib2 = Library()
lib3 = Library()

lib1.addBook("Test book")
lib2.addBook("Another Book")
lib3.addBook("OOP Programming")

book1 = Book(lib1, "Suf")
book2 = Book(lib2, "Elz")
book3 = Book(lib3, "Hay")




mem1 = Member("Sufyaan")

mem1.borrow(book1)
