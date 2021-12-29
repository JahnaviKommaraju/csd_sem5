# Suppose we have a number a, we have to find n, such that factorial of n (n!) is same as a. 
# As we know, the factorial n = n * (n - 1) * (n - 2) * ... * 1. If there is no such integer n then return -1.
# So, if the input is like a = 120, then the output will be 5.

a= int(input())
i = 1
while True:
    if a % i == 0:
        a //= i
    else:
        print('it is not a factorial')
        break
    if i > a:
        break
    i += 1
if a == 1:
    print(i)