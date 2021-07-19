# Write a program which can filter() to make a list whose elements are
# even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.

# Code

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(item):
    return item % 2 == 0


print(list(filter(even, my_list)))

# Alternative


def even(item):
    return item % 2 == 0


print(list(filter(even, range(1, 21))))

# Alternative

even = filter(lambda i: i % 2 == 0, range(1, 21))
print(list(even))

# Alternative

print(list(filter(lambda i: i % 2 == 0, range(1, 21))))
