from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculateArea(self):
        return self.side * self.side

newShape = Shape()
print(newShape.calculateArea())
newCircle = Circle(5)
print(newCircle.calculateArea())
newSquare = Square(4)
print(newSquare.calculateArea())