# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints
# Use try/except to catch exceptions.

# Code

def function():
    return 5/0

try:
    function()
except ZeroDivisionError as ze:
    print("The no is being devided by zero")
except:
    print("Caught an exception")