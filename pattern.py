def pattern(n,name):
    k = n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end="  "*((len(name)-2)//2))
        k = k-1
        for j in range(0,i+1):
            print(name,end="  ")
        print()


pattern(5,"jahnavi")


