# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example: If the following n is given as input to the program:
# 5

# Then, the output of the program should be:
# 3.55

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use float() to convert an integer to a float.
# Even if not converted it wont cause a problem because
# python by default understands the data type of a value.

# Code
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i/(i+1)
print(round(sum, 2))

# Alternative
n = int(input("Enter a number: "))
sum = 0.0
for i in range(1, n+1):
    sum += float(float(i)/(i+1))
print(sum)

# Alternative


def series(n):
    print(round(sum(map(lambda i: i/(i+1), range(1, n+1))), 2))


series(5)
