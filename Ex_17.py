# 17. Take two strings from the user and check whether removing one char from string 1 produces string 2 or not.
# For example:
# Input:
# s0 = ababab
# s1 = abbab
# Output:
# True
# (Since removing a(3rd element) from s0 produces s1)

# Input:
# s0='claps'
# s1='laps'
# output:
# True
def removeChar(string1, string2):
    if (len(string2)+1)!=len(string1):
        return False

    a,b=list(string1),list(string2)

    i=j=0
    while i<=len(a):
        if a[i]!=b[j]:
            a.pop(i)
            break
        i+=1
        j+=1
        
    if a==b:
        return True

string1 =input()
string2 = input()
print(removeChar(string1, string2))