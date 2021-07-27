# By using list comprehension, please write a program to print the list after removing
# the 0th,2nd,4th,6th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

# Code
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i % 2 != 0 and i <= 6]
print(li)

# Alternative
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i % 2 != 0 and i <= 6]
print(li)
