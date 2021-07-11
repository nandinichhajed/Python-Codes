# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# code

def check (elements):
    # all returns True if all digits i is even in element
    return all(ord(i) % 2 == 0 for i in elements)

# creates list of all given numbers with string data type
lt = [str(i) for i in range(1000, 3001)]
# filter removes element from list if check condition fails
lt = list (filter(check, lt))
print ("Even number between 1000 and 3000: ")
print(",".join(lt))

# Alternative
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))