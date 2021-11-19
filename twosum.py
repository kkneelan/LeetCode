class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compList = [target-num for num in nums]
        for x in range(len(nums)):
            var1 = nums[x] 
            if var1 in compList and x != compList.index(var1):
                return(x,compList.index(var1))        