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

class Designer(Employee):
    def __init__(self, name,age,salary,bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def bonus_(self):
        baseSalary = self.salary_()
        baseSalary += self.bonus

        return baseSalary

class Developer(Employee):
    def __init__(self, name,age,salary,bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def bonus_(self):
        baseSalary = self.salary_()
        baseSalary += self.bonus

        return baseSalary
    

m1 = Manager("Sufyaan", 23, 20000, 1000)
des1 = Designer("Ellie", 20, 15000, 500)
dev1 = Developer("Haya", 19, 12000, 350)

total1 = m1.bonus_()
print(f"Your Salary including your bonus is £{total1}")