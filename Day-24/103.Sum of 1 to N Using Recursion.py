# Given a number N.Find Sum of 1 to N Using Recursion

# Input
# 5

# Output
# 15

# Hints
# Make a recursive function to get the sum

# Code
n = int(input("Enter no to find sum: "))


def recurssion(n):
    if n == 0:
        return n
    return recurssion(n-1) + n


sum = recurssion(n)
print(sum)
