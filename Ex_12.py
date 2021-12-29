# Given a string s and an integer n, rearrange s into n rows so that s can be read vertically (top-down, left to right).
# Input:
# abcdefghi
# 5
# Read the input as a list of items list =[ "String", rows]
# Output:
# ['af', 'bg', 'ch', 'di', 'e']

num=int(input())
l=[input(),int(input())]
s=l[0]
n=l[1]
print([s[i::n] for i in range(n)])