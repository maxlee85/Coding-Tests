"""
Challenge:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

"""
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Solution:
Find the largest possible value in a subarray.
Iterate over array, if previous element is positive add that to current element.

    [-2,1,-3,4,-1,2,1,-5,4]
->  [-2,1,-3,4,-1,2,1,-5,4] # do nothing
        ^
->  [-2,1,-2,4,-1,2,1,-5,4] # add 1 to -3
           ^
->  [-2,1,-2,4,-1,2,1,-5,4] # do nothing
             ^            
->  [-2,1,-2,4,-1,2,1,-5,4] # add 4 to -1
                ^   
->  [-2,1,-2,4,3,2,1,-5,4] # add 3 to 2
                 ^   
->  [-2,1,-2,4,3,5,1,-5,4] # add 5 to 1
                   ^      
->  [-2,1,-2,4,3,5,6,-5,4] # add 6 to -5
                      ^     
->  [-2,1,-2,4,3,5,6,1,4] # add 1 to 4
                       ^
->  [-2,1,-2,4,3,5,6,1,5]
"""           

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] >= 0:
                nums[i]+=nums[i-1]
        return max(nums)
