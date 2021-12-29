# Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

## Test case- 1:
    # Input: nums = [0,1,0,3,12]
    # Output: [1,3,12,0,0]

## Test case- 2:
    # Input: nums = [0]
    # Output: [0]

## Test case- 3:
    # Input: prices = [1,0,1]
    # Output: [1,1,0]

def moveZeroes(nums):
       
        if len(nums)==1:
            return nums

        i=0
        j=0
        while(j<len(nums)):
            if  nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1

nums=[int(i) for i in input().split()]
moveZeroes(nums)
print(nums)

    