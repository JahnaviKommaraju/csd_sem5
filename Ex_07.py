# You are given a list of integers nums,mrepresenting a decimal number and nums[i] is between [0, 9].
# For example, [1, 3, 9] represents the number 139. 
# Return the same list in the same representation except modified so that 1 is added to the number.
# Example 1
#  Input
# nums = [1, 9, 1] 
# Output
# [1, 9, 2]
# Example 2
# Input
# nums = = [9]
# Output
# [1, 0]

def add_one(number):
    nums= [int(x) for x in str(number)]
    i = len(nums) - 1
    while i >= 0:
        if nums[i] + 1 <= 9:
            nums[i] = nums[i] + 1
            break
        else:
            nums[i] = 0
            i -= 1
    if i < 0:
        nums.insert(0, 1)
    nums= [str(x) for x in nums]  
    return nums

number=int(input())
print(add_one(number))  