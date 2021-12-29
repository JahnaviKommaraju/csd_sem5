x= int(input())
a = input()
b = input()
la = len(a)
lb = len(b)
f1 = [0] * 26
f2 = [0] * 26
l = 0
for i in range(la):
    f1[ord(a[i]) - ord('a')] += 1
for i in range(lb):
    f2[ord(b[i]) - ord('a')] += 1
for i in range(26):
    l += min(f1[i],f2[i])
print(l)