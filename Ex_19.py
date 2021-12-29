l=[25,10,5,1]

n=int(input())
a,b=0,0
while a<6:
    b=b+n//l[a]
    n=n%l[a]
    if n==0:
        break
    a+=1
print(b)