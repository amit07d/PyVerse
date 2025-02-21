# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def fuel_type(self):
        return "petrol or diesel"
        
    class ElectricalCar:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model  
        
        def full_name(self): 
            return f"{self.brand} {self.model}"
        
        def fuel_type(self):
            return "electric charge"
    
            
my_tesla = Car.ElectricalCar("Tata", "Muxu")
print(my_tesla.fuel_type())  
        
my_car = Car("Tesla", "M-3")
print(my_car.fuel_type()) 
