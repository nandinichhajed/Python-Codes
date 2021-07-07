# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# code
n = int(input('Enter the number to find factorial:'))
fact = 1
for i in range (1, n+1):
    fact = fact * i
print(fact)

# alternative
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input('Enter the number to find factorial:'))
print(f'{n}! is: {fact(n)} ')
