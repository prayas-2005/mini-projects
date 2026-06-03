# class student:
#     # default constructor
#     def __init__(self):
#         self.name = 'prayas'
#         self.age = 23

# s = student()
# print(s.name)
# print(s.age)


class Student:
    # parametrized constructor
    def __init__(self, name, id, city):
        self.name = name
        self.id = id
        self.city = city
    def printname(self):
        print(f"My name is {self.name}")
    
s = Student("prayas", 110, "Jaipur")
s.printname()
# print(s.name)
# print(s.id)
# print(s.city)