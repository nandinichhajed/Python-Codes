# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.

# code
s = str(input("Enter the string: "))
if s == "YES" or s == "Yes" or s == "yes":
    print("Yes")
else:
    print("No")

# Alternative
s = str(input("Enter the string: ").lower())
if s == "yes":
    print("Yes")
else:
    print("No")
