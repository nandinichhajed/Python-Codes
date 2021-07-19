# Write a program to generate and print another tuple
# whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

# Code
lst = list()
for i in range(1, 11):
    if i % 2 == 0:
        lst.append(i)

print(tuple(lst))

# Alternative
tpl = tuple(i for i in range(1, 11) if i % 2 == 0)
print(tpl)

# Alternative
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Lambda function returns True if found even element.
# Filter removes data for which function returns False
tpl1 = tuple(filter(lambda x: x % 2 == 0, tpl))
print(tpl1)
