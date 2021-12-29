# In a given string check if it has all the letters of the english alphabet and print 0.
#  If the string doesn't contain all the alphabets print the remaining alphabets
MAX_CHAR = 26
special_characters = "!@#$%^&* ()-+?_=,<>/"
def missingChars(Str):
    present = [False for i in range(MAX_CHAR)]
    for i in range(len(Str)):
        if (Str[i] >= 'a' and Str[i] <= 'z'):
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'):
            present[ord(Str[i]) - ord('A')] = True

    res = ""
    for i in range(MAX_CHAR):
        if (present[i] == False):
            res += chr(i + ord('a'))
    if res=="":
        return 0 		
    return res

Str = input()

print(missingChars(Str))
