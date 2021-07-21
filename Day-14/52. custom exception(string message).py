# Define a custom exception class which takes a string message as attribute.

# Hints
# To define a custom exception, we need to define a class inherited from Exception.

# Code

class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


error = MyError("something wrong")

# Alternative


class CustomException(Exception):

    def __init__(self, message):
        self.message = message


num = int(input("Enter a number: "))
try:
    if num < 10:
        raise CustomException("Input is less then 10")
    elif num > 10:
        raise CustomException("Input is greater then 10")
except CustomException as ce:
    print("THE ERROR RAISED :" + ce.message)
