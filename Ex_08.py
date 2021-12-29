# Remove all consecutive elements in a given string.
# Input:
# aabbcacabbaa


# Output:
# abcacaba


def rem_cons(str):
    n = len(str)
    if n <= 1:
         return str
    ans = str[0]
    for i in range(1, n):
        if str[i] != str[i-1]:
            ans += str[i]
    return ans


str = input()
print(rem_cons(str))