# class Myclass:
#     x = 4
#     y = 5
# obj = Myclass
# print(obj.x+obj.y)
# print(obj.x)
# print(obj.y)

# obj2 = Myclass
# obj3 = Myclass
# print(obj2.x)
# print(obj2.y)


# class fruits:
#     fruit = ["Apple", "Banana", "Orange"]

# obj = fruits()
# print(obj.fruit)


# class person:
#     name = "Luca"
#     age = 28
# p = person()
# print(f"Hello, My name is {p.name} and I am {p.age} years old.")


# class Person:
#     def __init__(self, name):
#         self.name = name
#         # self.age = age
        
#     def greets(self):
#         print("Hello, My name is " + self.name)
# p = Person("Emma")
# p.greets()
# print(p.name)
# print(p.age)

# class Calculator:
#     def add(self, a, b):
#         return a + b
    
#     def mul(self, a, b):
#         return a * b

# p = Calculator()
# print(p.add(5, 5))
# print(p.mul(12, 5))



# Inheritance
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)
    
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

p = Student("Prayas", "Saini")
p.printname()