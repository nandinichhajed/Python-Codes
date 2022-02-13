def greatest():
    if a > b:  
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
            
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

d = greatest()
print(f"The greatest number is {d}")