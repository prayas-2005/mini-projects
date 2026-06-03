# class Car:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
    
#     def move(self):
#         print("Drive the car")

# class Boat:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
    
#     def move(self):
#         print("Sail")

# class Plane:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
    
#     def move(self):
#         print("Fly")


# c = Car("ALTROZ", "TATA")
# b = Boat("Ibiza", "Touring 20")
# p = Plane("Boeing", "475")

# for x in (c, b, p):
#     x.move()



class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail")

class Plane(Vehicle):
    def move(self):
        print("Flying")
    
c = Car("ALTROZ", "TATA")
b = Boat("EBIZA", "TOURING 20")
p = Plane("BOEING", "747")

for x in (c, b, p):
    print(x.brand, ",",x.model)
    x.move()    
        