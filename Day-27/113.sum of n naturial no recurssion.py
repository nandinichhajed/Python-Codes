# sum(n) = n + sum(n-1)

def addition(n):
    if n == 0:
        return 0
    else:
        add = n + addition(n-1)
        return add

n = int(input("enter a number: "))
d = addition(n)
print(d)