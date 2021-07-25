# Please write a program to output a random number,
# which is divisible by 5 and 7, between 10 and 150
# inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.

# Code
import random
s = [i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]
print(random.choices(s))

# Alternative
# import random
# s = [i for i in range(10, 151) if i % 35 == 0 ]
# print(random.choices(s))