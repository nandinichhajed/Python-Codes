# With a given integral number n, 
# write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). 
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# code
n = int(input('Enter the number to Print Dictonary:'))
dictonary = {}
for i in range (1, n+1):
    dictonary[i] = i * i
print(dictonary)

# alternative
n = int(input('Enter the number to Print Dictonary:'))
dictonary={i : i*i for i in range (1, n+1)}
print(dictonary)