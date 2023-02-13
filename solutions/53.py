# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [nums[0]]
        res = arr[0]
        for i in range(1, len(nums)):
            arr.append(max(arr[i - 1] + nums[i], nums[i]))
            if arr[i] > res:
                res = arr[i]
        return res
