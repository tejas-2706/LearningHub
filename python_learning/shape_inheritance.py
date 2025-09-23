import math
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    

my_rect = Rectangle(2,3)
print(my_rect.area())
my_circle = Circle(3)
print(my_circle.area())