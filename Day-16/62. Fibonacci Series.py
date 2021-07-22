# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

# Example: If the following n is given as input to the program:

# 7
# Then, the output of the program should be:

# 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.

# Code
# n = int(input("Enter a number: "))
# f = lambda i : 0 if i == 0 else 1 if i == 1 else f(i-1)+f(i-2)
# print(','.join([str(f(i)) for i in range (0, n+1)]))

# Alternative
n = int(input("Enter a number: "))


def f(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return f(i-1)+f(i-2)


print(','.join([str(f(i)) for i in range(0, n+1)]))

# Alternative


def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]


n = int(input("Enter a number: "))
fibo = [0]*(n+1)                # initialize a list of size (n+1)
f(n)                            # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
# joining all string element of fibo with ',' character
ans = ",".join(fibo)
print(ans)
