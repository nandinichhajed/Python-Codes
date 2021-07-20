# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape
# where Shape's area is 0 by default.

# Hints
# To override a method in super class,
# we can define a method with the same name in the super class.

# Code
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)  # To print zero as default area
        self.length = l

    def area(self):
        return (self.length)**2


ar = Square(5)
print(ar.area())    # prints 25 as given argument

print(Square().area())  # prints zero as default area
