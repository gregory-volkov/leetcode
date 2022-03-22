# 539. Minimum Time Difference
# https://leetcode.com/problems/minimum-time-difference/submissions/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def str2num(s):
            h, m = int(s[:2]), int(s[3:])
            return h*60 + m
        mind = 24*60
        timePoints = sorted(map(str2num, timePoints))
        prev = timePoints[0]
        ans = mind - timePoints[-1] + timePoints[0]
        for point in timePoints[1:]:
            cur = point - prev
            if ans == 0:
                return ans
            if cur < ans:
                ans = cur
            prev = point
        return ans
