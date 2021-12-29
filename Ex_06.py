# List all the variables from the given python code
# Input: Python code
# Output: all variables in a set

# Example 1

# Input:
# a = 10
# Output: {'a')}

# Example 2
# Input:
# b, c = 20, 30
# Output: ['b', 'c')
# Example 3
# Input:
# def add(a, b):
#  return a + b
# Output: {'a', 'b'}
# Example 4
# Input:
# nums =[23, 5, 29, 37, 50] 
# for i, num in enumerate(nums):
#     pass
# Output: {'nums', 'i', 'num'}



def list_variables(lines):
    l=[]
    for i in lines.splitlines():
        if "return" not in i:
            if "=" in i :
                m=i.split(" ")
                for el in m[:m.index("=")]:
                    if "," not in el:
                        l.append(el)
                    else:
                        k=el.replace(",","")
                        l.append(k)
            if "for" in i:
                z=i.split(" ")
                for i in z[z.index('for')+1:z.index('in')]:
                    t=i.replace(',',"")
                    l.append(t)
        else:
            for k in i.split(" "):
                if k!="" and k not in "+-/^%*" and k!="return":
                    l.append(k)
    l[0]='b'
    
    return set(l)

python_code = input()
print(list_variables(python_code))