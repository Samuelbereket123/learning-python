class Vehicle:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.engine_on = False
    
    def start_engine(self):
        self.engine_on = True
        return f"The {self.make} {self.model} is now running"
    def display_info(self):
        return f"Make: {self.make} Model: {self.model} Year: {self.year}"
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
    def honk(self):
        return "beep beep"
        
    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, Doors: {self.num_doors}"
        
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):
        self.engine_on = True
        
        return f"The {self.make} {self.model} is running!"
        
print("### Vehicle Hierarchy Demonstration ###")

my_car = Car("Honda", "Civic", 2020, 3)
my_bike = Motorcycle("yamaha", "Iron 844", 2018, False)

print("\n--- Car Object (my_car) ---")
print(my_car.display_info())
print(my_car.start_engine())
print(my_car.honk())
print(f"Is the engine on? {my_car.engine_on}")
        
print("\n--- Car Mototrcycle (my_bike)---")     

print(my_bike.display_info())
print(my_bike.start_engine())
print(f"Has a sidecar? {my_bike.engine_on}")        
        
        
        
        
        
        