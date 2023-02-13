# 198. House Robber
# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rev = 0
        arr = [0 for _ in range(len(nums))]
        arr[0] = nums[0]
        if len(nums) > 1:
            arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
        
        return arr[-1]
