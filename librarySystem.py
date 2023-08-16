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




class Book(Library):
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
            print(f"You have borrowed {self.available}.")
        else:
            print(f"Sorry {self.title} has already been borrowed")



class Member(Library):
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []


    def borrowed(self, bookName):
        if bookName.available:
            bookName.borrowBook()
            self.borrowedBooks.append(bookName)
        else:
            print(f"Sorry {bookName.title} is unavailable")


lib1 = Library().addBook("Test Book")
lib2 = Library().addBook("Another book")
lib3 = Library().addBook("Big book")

book1 = Book(lib1, "Suf")
book2 = Book(lib2, "Elz")
book3 = Book(lib3, "Hay")

mem1 = Member("Sufyaan")
mem1.borrowed(lib2)