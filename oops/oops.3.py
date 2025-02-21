# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size =battery_size   
        
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_tesla = ElectricCar("Tesla", "Model 3", "85kwh")
print(my_tesla.full_name())
        
# my_car = Car("Tata", "Nexon")
# print(my_car.brand)
# print(my_car.full_name())
        
        