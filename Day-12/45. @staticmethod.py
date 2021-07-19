# Define a class named American which has a static method called printNationality.
# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.

# Code:
class America(object):
    @staticmethod
    def printNationality():
        print("I am an Indian")


american = America()
# this will not run if @staticmethod does not decorates the function.Because the class has no instance.
american.printNationality()


# this will run even though the @staticmethod does not decorate printNationality()
America.printNationality()
