# When the sum of N consecutive even numbers (where each number being added to the sum is denoted by Ei , 1<=i<N 
# is either a prime number or an even number it is called a happy number.
# You are given an integer input X.
# Write a program to find the sum S1,S2 ,S3 and so on of N consecutive even Integers,
# where the value of N keeps increasing by 1.You should continue the process until Ei <= X

#  Example 1:
# X=4
# N=1  sum=0
# N=2  0+2=2 
# N=3  0+2+4=6 
x=int(input())
print(x//2+1)
# def prime(xnum):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return True
#                 break
#     return False

# x=int(input())
# i=2
# sum=0
# while(i<x):
#     if(i%2==0 or prime(i)):
#         sum+=1
#     i+=2
# print(sum)