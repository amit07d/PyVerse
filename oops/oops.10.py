# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
class Battery:
    def __init__(self, battery_type):
        self.battery_type = battery_type
        
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        
class ElectricCar(Car, Battery,Engine):
    def __init__(self, brand, model, battery_type, engine_type):
        Car.__init__(self,brand,model)
        Battery.__init__(self, battery_type)
        Engine.__init__(self, engine_type)
        
my_tesla = ElectricCar("Maruti", "Model 3", "Lithium-Ion", "Dual-Engine")
print(my_tesla.brand)
print(my_tesla.battery_type)
print(my_tesla.engine_type)
        
my_car = Car("Toyota", "Glanza")
print(my_car.brand)