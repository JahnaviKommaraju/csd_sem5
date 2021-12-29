# Ancient Astronaut Theory

# You are given a string dictionary, representing a partial lexicographic ordering of ancient astronauts' dictionary.

# Given a string s, return whether it's a lexicographically sorted string according to this ancient astronaut dictionary, where the only constraint is that a comes before c which comes before b.

# Example 1:

# Input:

# aaaa h ccc i bbb

# Output

# True

string = input()
if string[::-1].index('b') < string[::-1].index('c') < string[::-1].index('a'):
    print("True")
else:
    print("False")