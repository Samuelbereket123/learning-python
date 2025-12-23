"""
So the word Polymorphism means 'many forms' so in programming it's referred to methods/function/operators with the same name that can be excuted on many classes and objects.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def Move(self):
        print("Move")

class Car:
    pass 

class Boat(Vehicle):
   def Move(self):
       print("Move boat")      
class Plane(Vehicle):
   def Move(self):
       print("Move Plane")      

boat1 = Boat("IDK", 3003)
plane1 = Plane("IDKKK", 111)

for x in (boat1, plane1):
    print(x.brand)
    print(x.model)
    x.Move()

""" Might not be the best example but we don't care. """