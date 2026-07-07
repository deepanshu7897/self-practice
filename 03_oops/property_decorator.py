class Car:
     total_cars = 0
     def __init__(self, userbrand, usermodel):
          self.__brand = userbrand
          self.__model = usermodel
          Car.total_cars +=1
     def get_brand(self) :  
          return self.__brand + "!"  
     def full_name(self):
          return f"{self.__brand} {self.__model}"    
     def fuel_type(self):
          return "petrol or diesel" 
      
     @staticmethod #decorator
     def general_description():
          return "cars are means of transport"
     @property
     def model(self):
          return self.__model
class ElectricCar(Car) :
     def __init__(self , brand , model , battery_size):
          super().__init__(brand , model)
          self.battery_size = battery_size
     def fuel_type():
          return "electric charge"       
#my_tesla = ElectricCar("tesla", "model s", "85kw")
#print(my_tesla.get_brand())
#print(my_tesla.model)
#print(my_tesla.full_name())
#print(my_tesla.fuel_type())
#safari = Car("tata", "safari")
#print(safari.fuel_type)


          
my_car = Car("Toyota", "Camry")
#print(my_car.general_description())
#print(Car.general_description())
#print(my_car.brand)   
#print(my_car.model) 
#my_new_car = Car("Honda", "Civic")
#print(my_new_car.brand)  
#print(Car.total_cars)
#my_car.model = "city"
print (my_car.model)