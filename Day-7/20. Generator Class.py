# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:
# 7

# Then, the output should be:
# 0
# 7
# 14

# Code
class my_generators():
    def generator_function(self, n):
        for i in range(0, int(n/7)+1):
            yield i * 7

         # class         # function
for i in my_generators().generator_function(int(input("Enter a no: "))):
    print(i)
