# Define a class which has at least two methods:
# getString: t get a string from console inpout
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# code
class IO (object):

    def __init__ (self):
        self.s = ''
    
    def getString(self):
        self.s = input('Enter String:')
    
    def printString(self):
        print(self.s.upper())

str_obj = IO()
str_obj.getString()
str_obj.printString()