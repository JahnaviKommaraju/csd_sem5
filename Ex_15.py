# A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly. 
# If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number.
# Input:
# 32
# Output:
# 32 is a happy number

def Happynum(n):    
    t=r = 0    
    while(n > 0):    
        r = n%10;    
        t+= (r*r)   
        n = n//10 
    return t
        
num = int(input()) 
temp = num
while(temp!= 1 and temp!= 4):    
    temp=Happynum(temp)
if(temp== 1):    
    print(str(num) + " is a happy number");    
elif(temp == 4):    
    print(str(num) + " is not a happy number")