# You are given an integer, N.
# Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:
# size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# Hints
# First print the half of the Rangoli in the given way and save each line in a list.
# Then print the list in reverse order to get the rest.

# Code

# import string

import string


def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input("Enter the no of Alphabets: "))
    print_rangoli(n)

# Alternative


def rangoli(n):
    # your code goes here
    l1 = list(map(chr, range(97, 123)))
    x = l1[n-1::-1]+l1[1:n]
    mid = len('-'.join(x))
    for i in range(1, n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid, '-'))
    for i in range(n, 0, -1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid, '-'))


rangoli(5)
