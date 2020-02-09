"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

[0,0,1,1,1,2,2,3,3,4] returns 5
"""

# remove dupes
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i+=1
        return len(nums)
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

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
    
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(nums):
            comp = target - value
            if comp in my_dict:
                return [index, my_dict[comp]]
            else:
                my_dict[value] = index
