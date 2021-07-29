# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

# Hints
# Use for loop to iterate all possible solutions.

# Code
def animals(heads, legs):
    s = 'No solutions!'
    for i in range(heads + 1):
        j = heads-i
        if i * 2 + j * 4 == legs:
            return i, j
    return s, s


heads = int(input("Enter no of Heads: "))
legs = int(input("Enter no of Leags: "))
count = animals(heads, legs)
print(count)
