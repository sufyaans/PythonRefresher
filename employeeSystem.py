'''
Create a class called Employee with attributes like name, age, and salary. 
Implement methods for salary calculation and printing employee information. 
Then, create subclasses for different types of employees like Manager, Developer, and Designer.
'''

class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def salary_(self):
        multiplier = 2 
        # self.position = position

        # if position == "Manager":
        #     multiplier = 3
        # elif position == "Developer":
        #     multiplier = 6
        # elif position == "Designer":
        #     multiplier = 9

        annualSalary = self.salary * multiplier        
        return annualSalary
    

class Manager(Employee):
    def __init__(self, name,age,salary,bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def bonus_(self):
        baseSalary = self.salary_()
        baseSalary += self.bonus

        return baseSalary


