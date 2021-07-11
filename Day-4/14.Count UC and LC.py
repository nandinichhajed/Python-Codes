# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:
# Hello world!

# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# code
word = input("Enter a string with both uppercase and lowercase: ")
upper, lower = 0,0

for i in word:
    if 'a' <= i and i <= 'z':
        lower += 1
    if 'A' <= i and i <= 'Z':
        upper += 1

print(f"UPPER CASE {lower}\nLOWER CASE {upper}") 

# Alternet 
word = input()
upper,lower = 0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

print(f"UPPER CASE {lower}\nLOWER CASE {upper}")

# Alternet 
word = input()
upper = sum(1 for i in word if i.isupper())  # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print(f"UPPER CASE {lower}\nLOWER CASE {upper}")