# Creating a Class

class Car:
    # Constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} car is driving.")



my_car = Car("Toyota", "White") # Create a object instance
my_car.drive()

# self refers to this object.
# Attributes belong to each instance: my_car.brand, my_car.color.



# Inheritance
# super() lets you reuse the parent’s initialization.

class ElectricCar(Car):
    def __init__(self, brand, color, battery,mileage):
        super().__init__(brand, color)
        self.battery = battery
        self._mileage = mileage

    def charge(self):
        print(f"Charging {self.battery} kwh battery")

battery_car = ElectricCar("MG", "Black", "90","12")

battery_car.charge()

print(battery_car.brand)
print(battery_car._mileage)



# Encapsulation & Methods

# Keep related data & logic together.
# “Private” attributes are by convention prefixed with _



# Special (“Dunder”) Methods
# Python lets you customize built-in behaviors.

class Point:
    def __init__(self,x,y):
        self.x,self.y = x,y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    

p1 = Point(2,3)
p2 = Point(4,1)
p3 = Point(4,1)

print(p1+p2+p3)
