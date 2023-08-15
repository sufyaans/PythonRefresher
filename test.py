
'''
Create a class named Person with attributes "name" and "age". 
Define a constructor to initialize these attributes and a method called "introduce" that prints out a message introducing the person. 
Create an instance of the class and call the "introduce" method.
'''
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hello my name is {self.name}, and I am {self.age} years old")


# p1 = Person("Sufyaan", 23)
# p1.introduce()


'''
Create a class named "Rectangle" with attributes "width" and "height". 
Implement methods to calculate the area and perimeter of the rectangle. 
Create an instance of the class, set the width and height, 
and then print out its area and perimeter.
'''
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def calc(self):
#         total = self.width * self.height
#         return total
    

# rec1 = Rectangle(10,15)
# print(rec1.calc())

'''
Create a class named Student with attributes "name", "age", and "grade". 
Implement a method called "display_info" that prints out the student's "name", "age", and "grade". 
Create multiple instances of the class with different information and call the display_info method for each instance.
'''
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade #0-100

#     def display_info(self):
#         print(f"My name is {self.name} and I am {self.age} years old. In my class I got {self.grade}/100")

# s1 = Student("Sufyaan", 23, 67)
# s2 = Student("Ellie", 20, 80)
# s3 = Student("Haya", 24, 53)
# s1.display_info()
# s2.display_info()
# s3.display_info()


'''
Create a class named BankAccount with attributes account_number and balance. 
Implement methods for "depositing" and "withdrawing" money from the account. Make sure to update the "balance" accordingly. 
Create an instance of the class, deposit some money, withdraw some money, and print the final balance.
'''

# class BankAccount:

#     account_number_check = int(input("Please enter your account number: "))

#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance


#     def deposit(self, deposit):
        
#         if BankAccount.account_number_check == self.account_number:
            
#             self.deposit = deposit
#             self.balance += deposit
#             print(f"Your updated balance is £{self.balance}")
#         else:
#             print("Incorrect account number, Please try again")

    
#     def withdraw(self, withdraw):
        
#         if BankAccount.account_number_check == self.account_number:
#             print(f"Your current balance is £{self.balance}")
#             self.withdraw = withdraw
#             if self.withdraw > self.balance:
#                 print("Insufficient funds, Try again")
#             else:
#                 self.balance -= withdraw
#                 print(f"You have successfully withdrew £{withdraw}, your updated balance is £{self.balance}")

#         else:
#             print("Incorrect account number, Please try again")

# depositAmount = int(input("How much would you like to deposit £"))     
# withdrawAmount = int(input("How much would you like to withdraw £"))
# b1 = BankAccount(20984167, 400)

# b1.deposit(depositAmount)
# b1.withdraw(withdrawAmount)


'''
Create a class named "Car" with attributes "make", "model", and "year". 
Implement a method called "display_info" that prints out the car's "make", "model", and "year". 
Create multiple instances of the class with different information and call the "display_info" method for each instance.
'''

# class Car:
#     def __init__(self, make, model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Your car is a {self.make} {self.model} released in {self.year}")

# c1 = Car("VW", "Golf", 2008)
# c1.display_info()


'''
Create a class named "Circle" with an attribute "radius". 
Implement methods to calculate the "area" and "circumference" of the circle. 
Create an instance of the class, set the "radius", and then print out its "area" and "circumference".
'''

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self, pi):
#         area = pi * self.radius * self.radius
#         return area
#     def circ(self, pi):
#         circ = 2 * pi * self.radius
#         return circ
    
#     def output(self):
#         print(f"The circumference of the circle is: {Circle.circ(self, pi)}")
#         print(f"The area of the circle is: {Circle.area(self, pi)}")

# pi = 3.142
# cir1 = Circle(12)
# cir1.output()


'''
Create a class named Dog with attributes name and breed. 
Define a method called bark that prints a message like "Woof! Woof!" for the given dog. 
Create multiple instances of the class with different names and breeds and call the bark method for each instance.
'''

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.noise = "Woof! Woof!"
       

#     def noise_(self):
       
#         if self.name == "Ellie":
#             self.noise = "Meow"
#         elif self.name == "Suf":
#             self.noise == "Woof! Woof!"
#         else:
#             self.noise ="kakaka"


#     def output(self):
#         print(f"{self.name} says {self.noise}")


# d1 = Dog("Jack", "Something")
# d1.noise_() 
# d1.output()


'''
Create a class named "Book" with attributes "title", "author", and "publication_year". 
Implement a method called "get_info" that returns a formatted string containing the book's information. 
Create an instance of the class and call the "get_info" method to display the book's details.
'''

# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def get_info(self):
#         print(f"\n Book: {self.title} \n Author: {self.author} \n Publish Year: {self.publication_year} \n")


# book1= Book("TKAMB", "Earnest", 1943)
# book1.get_info()


'''
Create a class named Rectangle similar to Question 2, but this time, 
implement a method called is_square that checks whether the rectangle is a square or not based on its width and height. 
Create instances of the class with different dimensions and test the is_square method.
'''

# class Rectangle:

#     def __init__(self, width, height):
#         self.height = height
#         self.width = width

#     def area(self):
#         areaCalc = self.height * self.width
#         return areaCalc
    
#     def perimeter(self):
#         periCalc = (self.height * 2) + (self.width *2)
#         return periCalc
    
#     def isSquare(self):

#         if self.height == self.width:
#             print("This is a Square")
#         else:
#             print("This is not a square")


# r2 = Rectangle(10,15)
# r2.perimeter()
    

'''
Create a class named "Bank" that represents a simple bank with a "list of accounts". 
Implement methods to "add an account", "deposit money" into an account, "withdraw money" from an account, 
and "display account information". Test these methods by adding accounts, depositing, and withdrawing money.
'''

class BankAccount:
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):            
        self.balance += amount
        print(f"Your updated balance is £{self.balance}")


    
    def withdraw(self, amount):
        print(f"Your current balance is £{self.balance}")
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds, Try again")
        else:
            self.balance -= amount
            print(f"You have successfully withdrew £{amount}, your updated balance is £{self.balance}")


class Bank:

    def __init__(self):
        self.accountList = []

    def addAccount(self, newAccount):
        self.accountList.append(newAccount)
        return self.accountList
    
    def deposit(self, account_number, amount):
        for account in self.accountList:
            if account.account_number == account_number:
                account.deposit(amount)
                return
            else:
                print("account not found")

    def withdraw(self, account_number, amount):
        for account in self.accountList:
            if account.account_number == account_number:
                account.withdraw(amount)
                return
            else:
                print("account not found")
                

b1 = Bank()

acc1 = BankAccount(account_number=20984167, balance=400)

b1.addAccount(acc1)

b1.deposit(20984167, 300)
b1.withdraw(20984167, 300)