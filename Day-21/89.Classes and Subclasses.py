# Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print
# "Male" for Male class and "Female" for Female class.

# Hints
# Use Subclass(Parentclass) to define a child class.

# Code
class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


male = Male()
female = Female()
print(male.getGender())
print(female.getGender())

# Alternative


class Person(object):
    def __init__(self):
        self.gender = "unknown"

    def getGender(self):
        print(self.gender)


class Male(Person):
    def __init__(self):
        self.gender = "Male"


class Female(Person):
    def __init__(self):
        self.gender = "Female"


female = Female()
male = Male()
female.getGender()
male.getGender()
