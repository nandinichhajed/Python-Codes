# Define a function which can generate and print a tuple
# where the value are square of numbers between 1 and 20 (both included).
# Hint:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

# code

def square():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
    print(tuple(li))


square()

# Alternative


def square():
    li = [i**2 for i in range(1, 21)]
    print(tuple(li))


square()
