# Return frequency of words in a given string.

# Input:

# Apple Mango Orange Mango Guava Guava Mango

# Output:

# The frequency of  Apple is  1

# The frequency of  Mango is  3

# The frequency of  Orange is  1

# The frequency of  Guava is 2
   
string= input()
words = string.split()
unique_words = set(words)
for w in unique_words :
    print('The frequency of ', w , 'is :', words.count(w))
