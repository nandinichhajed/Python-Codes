# By using list comprehension, please write a program to print the list
# after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.

# Code
lst = [12, 24, 35, 70, 88, 120, 155]
lst = [x for x in lst if x % 35 != 0]
print(lst)

# Alternative
li = [12, 24, 35, 70, 88, 120, 155]
lst = list(filter(lambda x: x % 35 != 0, li))
print(lst)
