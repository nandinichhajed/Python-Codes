# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
# first half values in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

# code
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tp1 = tup[:5]
tp2 = tup[5:]

print(tp1)
print(tp2)

# Alternative
lst1 = []
lst2 = []

for i in range(0, 10):
    lst1.append(i)
    lst2.append(i)
print(tuple(lst1[:5]))
print(tuple(lst2[5:]))

# Alternative
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst = int(len(tup)/2)
print(tuple(tup[:lst]))
print(tuple(tup[lst:]))

# Alternative
tup = [i for i in range(1, 11)]
print(f'{tuple(tup[:5])} \n{tuple(tup[5:])}')
