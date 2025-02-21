# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand
    
my_car = Car("Tata", "Nexon")
print(my_car.get_brand())

my_car.set_brand("Mahindra")
print(my_car.get_brand())