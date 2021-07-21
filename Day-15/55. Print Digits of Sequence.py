# Write a program which accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.

# Example: If the following words is given as input to the program:
# 2 cats and 3 dogs.

# Then, the output of the program should be:
# ['2', '3']

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints
# Use re.findall() to find all substring using regex.

# Code
import re
s = input("Enter a string seperated with spaces: ")
print(re.findall("\d+", s))

# Alternative
s = input("Enter a string seperated with spaces: ").split()
dig = []
for word in s:
    if word.isdigit():  # isnumeric() / isdecimal()
        dig.append(word)
print(dig)

# Alternative
s = input("Enter a string seperated with spaces: ").split()
dig = [word for word in s if word.isdigit()]  # using list comprehension method
print(dig)
