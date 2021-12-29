# Given an integer n, return a list with each number from 1 to n, 
# except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".

# Note: return the number as a

# string.

# Example 1:

# Input:
# n = 16
# Output:
# ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]

##########  APPROACH 1 #############

def Claps(n):

    l=[]
    for i in range(1,n+1):
        if i%3==0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
            l.append('clap')
        else:
            l.append(str(i))
    return l

n=int(input())
print(Claps(n))



##########  APPROACH 2 #############

# def Claps(n):
#   res=[str(i) for i in range(1,n+1)]
#   for i in range(len(res)):
#     if int(res[i])%3==0:
#       res[i]='clap'
#     elif '3' in res[i] or '6' in res[i] or '9' in res[i]:
#       res[i]='clap'
#   return res

# n=int(input())
# print(Claps(n))