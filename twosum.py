# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compList = [target-num for num in nums]
        for x in range(len(nums)):
            var1 = nums[x] 
            if var1 in compList and x != compList.index(var1):
                return(x,compList.index(var1))        
