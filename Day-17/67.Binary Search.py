# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

# Hints
# Use if/elif to deal with conditions.

# Code


def binary_search_Ascending(list, target):
    lower = 0
    upper = len(list)
    print('List Length:', upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Middle Value:', x)
        value = list[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x


list = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]
print('The Value Found at Index:', binary_search_Ascending(list, 82))
