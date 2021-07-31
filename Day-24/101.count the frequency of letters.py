# You are given a string.Your task is to count the frequency of letters
# of the string and print the letters in descending order of frequency.

# If the following string is given as input to the program:
# aabbbccde

# Then, the output of the program should be:
# b 3
# a 2
# c 2
# d 1
# e 1

# Hints
# Count frequency with dictionary and sort by Value from dictionary Items

# Code
s = input("Enter string: ")
dictonary = {}
for i in s:
    dictonary[i] = dictonary.get(i, 0) + 1

dictonary = sorted(dictonary.items(), key=lambda x: (-x[1], x[0]))
for i in dictonary:
    print(i[0], i[1])
