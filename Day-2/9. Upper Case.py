# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# Code
def user_input():
    while True:
        s = input("Enter a String: ")
        if not s:
            return
        yield s

for line in map(str.upper, user_input()):
    print(line)