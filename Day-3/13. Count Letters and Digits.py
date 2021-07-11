# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:
# hello world! 123

# Then, the output should be:
# LETTERS 10
# DIGITS 3

word = input("Enter a string with numbers: ")
letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\nDIGIT {digit}") 