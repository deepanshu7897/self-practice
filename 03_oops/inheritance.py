class Car:
     def __init__(self, userbrand, usermodel):
          self.brand = userbrand
          self.model = usermodel
     def full_name(self):
          return f"{self.brand} {self.model}"    
class ElectricCar(Car) :
     def __init__(self , brand , model , battery_size):
          super().__init__(brand , model)
          self.battery_size = battery_size
my_tesla = ElectricCar("tesla", "model s", "85kw")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())


          
my_car = Car("Toyota", "Camry")
print(my_car.brand)   
print(my_car.model) 
my_new_car = Car("Honda", "Civic")
print(my_new_car.brand)  