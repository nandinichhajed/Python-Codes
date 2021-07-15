# Define a class, which have a class parameter and have a same instance parameter.
# Hints:
# Define an instance parameter,
# need add it in __init__ method.
# You can init an object with construct parameter or set the value later

#  Code
class Food:
    # Defining the class parameter "name"
    name = "Food"

    def __init__(self, name=None):
        # self.name is instance parameter
        self.name = name


pasta = Food("Pasta")
print("%s name is %s" % (Food.name, pasta.name))

Pizza = Food()
Pizza.name = "Pizza"
print("%s name is %s" % (Food.name, Pizza.name))
