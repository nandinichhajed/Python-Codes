# Write a program which can map() and filter() to make a list whose elements are
# square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Code

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(item):
    return item ** 2


def even(items):
    return items % 2 == 0


print(list(map(square, filter(even, my_list))))


# Alternative
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, my_list))
print(list(evenNumbers))
