class Person:

    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def pr(self, name, age):
        print(f"my name is {Person.name}")


p1= Person("Sufyaan", 21)

print(p1.pr())