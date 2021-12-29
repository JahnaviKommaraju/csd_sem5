# Take the number from the user, reverse it and add it to itself. If the sum is not a palindrome, 
# then repeat the procedure until you get a palindrome.

# Input:

# 18

# Output:

# Palindrome found at 99

num = int(input())

while True:
    rev = int(str(num)[::-1])
    if num+rev == int(str(num+rev)[::-1]):
        print("Palindrome found at",num+rev)
        break
    else:
        num+=rev