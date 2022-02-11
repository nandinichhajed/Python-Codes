a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
d = int(input("enter number: "))
print(a, b, c, d)

if(a>d):
    f1 = a
else:
    f1 = d
    
if(b>c):
    f2 = b
else:
    f2 = c

if (f1>f2):
    print(f1)
else:
    print(f2)