# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# Code

class Circle():
    def __init__(self, r):
        self.radious = r

    def area(self):
        return 3.14*(self.radious**2)


circle = Circle(5)
print(circle.area())
