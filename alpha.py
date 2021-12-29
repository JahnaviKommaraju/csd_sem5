str=input().lower()
if str.isalpha():
    print('zero')
else:
    for i in str:
        if i==" ":
            print('zero',end="")
        if not i.isalpha():
            print(i,end="")