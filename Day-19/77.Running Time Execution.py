# Please write a program to print the running time of execution of "1+1" for 100 times.

# Hints
# Use timeit() function to measure the running time.

# Code
import time
from timeit import Timer
t = Timer("for i in range(100): 1+1")
print(t.timeit())

# Alternative

before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution = after - before
print(execution)
