# 2576. Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        mid = len(nums)//2
        i, j = 0, mid
        res = 0
        nums = sorted(nums)
        while i < mid and j < len(nums):
            if nums[j] >= nums[i]*2:
                res += 2
                i += 1
            j += 1
        return res
