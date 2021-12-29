# Given two non-negative integers n1 and n2, where n1<n2. The task is to find the total number of integers in the range interval [n1, n2] (both inclusive) 
# which have no repeated digits.

# For example:
# Suppose n1 = 11 and n2 = 15.
# There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

# Example 1:
# Input:
# 11 --- Value of n1
# 15 --- Value of n2

# Output:
# 4


def repeated_digit(n):
    arr = []
    while n != 0:
        d = n%10
        if d in arr:
            return 0
        arr.append(d)
        n = n//10 
    return 1

n1,n2= map(int, input().split())
if n1<n2:
    count= 0
    for i in range(n1, n2+1):
        count+=repeated_digit(i) 
    print(count)

else:
    print('condition is not satisfied')
