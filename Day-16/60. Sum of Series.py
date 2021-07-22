# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:
# 5

# Then, the output of the program should be:
# 500

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.

# Code

def function(n):
    if n == 0:
        return 0
    return function(n-1)+100


n = int(input("Enter a number: "))
print(function(n))

# Alternative
n = int(input("Enter a number: "))
def f(x): return f(x-1)+100 if x > 0 else 0


print(f(n))
