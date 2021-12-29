# Given an array of integers and an integer “K”. Return an array of integers keeping the
#  first element in the given array intact and the cyclical rotation of the successive elements. 

# For example:
# Example 1:
# Arr[] = {10, 20, 30, 40, 50} and K = 2 (Two cyclical rotations)
# After 1st rotation = {10, 50, 20, 30, 40}
# After 2nd rotation = {10, 40, 50, 20, 30}

# Example 2:
# Arr[] = {10, 20, 30, 40} and K = 1 (One cyclical rotation)
# After 1st rotation = {10, 40, 20, 30}

# Example 3:
# Arr[] = {10, 20, 30} and K = 4 (four cyclical rotations)
# After 1st rotation = {10, 30, 20}
# After 2nd rotation = {10, 20, 30}
# After 3rd rotation = {10, 30, 20}
# After 4th rotation = {10, 20, 30}

# Constraints:
# 1 < N < = 100
# -100 < = Arr[i] < = 100
# 1 < = K < = 100

arr=[int(i) for i in input().split()]  #list comprehension for list input in single line with spaces  10 20 30 40 50
k=int(input())
for i in range(k):
    prev = arr[-1]
    for j in range(1,len(arr)):
        arr[j], prev = prev,arr[j]  
print(arr)