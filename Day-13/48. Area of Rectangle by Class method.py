# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# Code
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rect = Rectangle(2, 10)
print(rect.area())
