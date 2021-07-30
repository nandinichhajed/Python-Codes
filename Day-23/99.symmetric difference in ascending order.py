# Given 2 sets of integers, M and N,
# print their symmetric difference in ascending order.
# The term symmetric difference indicates those values
# that exist in either M or N but do not exist in both.

# Input
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
# 4
# 2 4 5 9
# 4
# 2 4 11 12

# Output
# Output the symmetric difference integers in ascending order, one per line.
# 5
# 9
# 11
# 12

# Hints
# Use '^' to make symmetric difference operation.

# Code
if __name__ == '__main__':
    n = int(input("Enter no of integer and the following integers: "))
    setA = set(map(int, input().split()))

    m = int(input("Enter no of integer and the following integers: "))
    setB = set(map(int, input().split()))

    ans = list(setA ^ setB)
    ans.sort()
    print("The symmetric difference integers in ascending order is:")
    for i in ans:
        print(i)
