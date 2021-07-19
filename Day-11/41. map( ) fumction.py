# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use lambda to define anonymous functions.

# Code
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(item):
    return item ** 2


print(list(map(square, my_list)))

# Alternative


def square(item):
    return item ** 2


lst = [i for i in range(1, 11)]
print(list(map(square, lst)))

# Alternative
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = map(lambda x: x**2, my_list)
print(list(square))
