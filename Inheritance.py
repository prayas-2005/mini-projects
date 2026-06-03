# class Person:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
    
#     def printname(self):
#         print(self.name, self.city)
    
# class Student(Person):
#     pass

# p = Student("Elexa", "Berlin")
# p.printname()


# parent class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
    
#     def move(self):
#         return "move forward!"

# # child class
# class car(Vehicle):
#     def honk(self):
#         return "Beep beep!"
    
# p = car("Tata")
# print(p.honk())


class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)
    
class Father:
    fathername = ""
    
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father : ", self.fathername)
        print("Mother : ", self.mothername)


s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
