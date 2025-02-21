# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model
    
    @property
    def model(self):
        return self._model

    
my_car = Car("Toyota", "corolla")
print(my_car.model)


# my_new_car = Car("Tesla", "Xuv")
# print(my_new_car.model)