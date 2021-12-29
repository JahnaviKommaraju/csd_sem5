# A number ‘n’ is called Bleak if it cannot be represented as a sum of a positive number x 
# and a number of 1s in binary of x. Check if a number is Bleak.


# Example 1:
# Input:
# 16
# Output:

# 16 is a supported number at 13

n = list(map(int, input().split()))
for j in n:
    for i in range(1, j):
        temp = bin(i)
        if i+str(temp).count('1')==j:
            break
    else:
        print(j," is a bleak number")