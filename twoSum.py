"""
Challenge:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

"""
Example:
nums = [2, 7, 11, 15]
target = 9
return [0, 1]

Because nums[0] + nums[1] = 2 + 7 = 9,

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
