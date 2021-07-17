# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.
# Hint:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# code
def square():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
    print(li[5:])


square()

# Alternative


def square():
    li = [i**2 for i in range(1, 21)[5:]]
    print(li)


square()
