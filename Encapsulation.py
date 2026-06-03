class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private property
        
    # getter method used for access private property
    def get__age(self):
        return self.__age
        
s = Student("Prayas", 23)
# print(s.name) 
# print(s.__age)
print(s.get__age())