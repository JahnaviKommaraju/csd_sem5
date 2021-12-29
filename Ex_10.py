# Given a string STR which contains numbers (0 to 9) and also letters of English alphabet (A to Z and a to z). 
# the task is to reverse the string in such a way that the positions of numbers in the string are left unaltered

# Example :

# Input : a1b2igh3 ---- Value of STR

# Output: h1g2iba3

def reverseOnlyLetters(S):
    letters = [ele for ele in S if ele.isalpha()]
    ans = []
    for ele in S:
        if ele.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(ele)
    return "".join(ans)

str=input()
print(reverseOnlyLetters(str))