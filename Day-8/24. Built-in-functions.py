# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
# And add document for your own function

# code

print(abs.__doc__)
print(input.__doc__)
print(int.__doc__)


def pow(n, p):
    return n ** p


print(pow(3, 2))
print(pow.__doc__)
