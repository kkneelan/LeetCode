# You are given an integer array nums with the following properties:
# 
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        setList = set(nums)
        for x in setList:
            if nums.count(x) == n:
                return x