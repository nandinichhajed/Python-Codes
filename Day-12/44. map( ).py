# Write a program which can map() to make a list whose elements are
# square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Code
def square(item):
    return item ** 2


lst = [i for i in range(1, 21)]
print(list(map(square, lst)))

# Alternative

print(list(map(lambda i: i ** 2, range(1, 21))))
