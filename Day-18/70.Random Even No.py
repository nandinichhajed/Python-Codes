# Please write a program to output a random even number
# between 0 and 10 inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.

# Code
import random
s = [i for i in range(11) if i % 2 == 0]
print(random.choices(s))
