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
                
