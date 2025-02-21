# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
my_tesla = ElectricCar("Tesla", "TM-3", "85kwh")
# print(my_tesla.model,":",my_tesla.brand)
    
my_car = Car("Toyota", "xuv")
# print(my_car.model)



print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_car, Car))