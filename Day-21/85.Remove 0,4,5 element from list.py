# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

# Code
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i not in (0, 4, 5)]
print(li)

# Alternative
li = [12, 24, 35, 70, 88, 120, 155]
print(list(j for i, j in enumerate(li) if i != 0 and i != 4 and i != 5))
