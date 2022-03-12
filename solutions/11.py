# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        cur_max = min(height[l], height[r]) * (r - l)
        while r != l:
            if height[r] > height[l]:
                l += 1
                cur_sq = min(height[l], height[r]) * (r - l)
            else:
                r -= 1
                cur_sq = min(height[l], height[r]) * (r - l)
            if cur_sq > cur_max:
                cur_max = cur_sq
        return cur_max
