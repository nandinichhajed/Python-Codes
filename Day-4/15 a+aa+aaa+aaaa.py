# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:
# 9

# Then, the output should be:
# 11106

a = input("Enter a number: ")
print(sum(int(i*a) for i in range(1,5)))

# Alternative
a = input("Enter a number: ")
total = 0
temp = str()
for i in range (4):
    temp += a             # concatenating 'a' to 'tmp'
    total += int(temp)    # converting string type to integer type
print(total)

# Alternative
a = input("Enter a number: ")
# N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)