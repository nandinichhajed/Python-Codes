# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.

# Example: If the following n is given as input to the program:
# 10

# Then, the output of the program should be:
# 0,2,4,6,8,10

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use yield to produce the next value in generator.

# Code
n = int(input("Enter a number: "))
values = []


def EvenGenerator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
