# Given a string (str) find the score of str as per the following rules 
# - for each palindrome of length 4 in str , add 5 as score
# -for each palindrome of length  5in str , add 10 as score
# -palindrome can overlap within str but must not be circular (ie they may not wrap around the end of the string)
# Initial score =0 no white spaces in the string.
# Ex- 'ABCBAAAA'
# Score = 15
# ABCBA-10 
# AAAA-5

str= input()
n=len(str)
res=[]
score=0
for i in range(n):
    for j in range(i+1,n+1):
        temp=str[i:j]
        if temp==temp[::-1]:
            res.append(str[i: j])
            if len(temp) == 4:
                score+=5
            if len(temp) == 5:
                score+=10    
print(score)
