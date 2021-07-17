# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.

# Code
def square():
    d = dict()
    for i in range(1, 21):
        d[i] = i**2
    print(d)


# square()

# Alternative


def square():
    # Using comprehension method
    dict = {i: i ** 2 for i in range(1, 21)}
    print(dict)


square()
