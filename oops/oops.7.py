# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    @staticmethod
    def general_description():
        return "Cars are means of transport" 
        
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size =battery_size   
    
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
print(Car.general_description())
    
# my_car = ElectricCar("Tesla", "Model 3", "85kwh")
# print(my_car.full_name())