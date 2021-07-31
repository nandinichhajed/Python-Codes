# Write a Python program that accepts a string and calculate
# the number of digits and letters.

# Input
# Hello321Bye360

# Output
# Digit - 6
# Letter - 8

# Hints
# Use isdigit() and isalpha() function

# Code
n = input("Enter String: ")
dig, letter = 0, 0
for i in n:
    dig += i.isdigit()
    letter += i.isalpha()
print('Digit:-', dig)
print('Letter:-', letter)
