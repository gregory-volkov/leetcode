# 1937. Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        subs = {}
        lft, rgt = [0 for _ in range(m)], [0 for _ in range(m)]
        
        for i in range(1, n):
            lft[0] = points[i - 1][0]
            rgt[m - 1] = points[i - 1][m - 1]
            for j in range(1, m):
                lft[j] = max(lft[j - 1] - 1, points[i - 1][j])
            for j in range(m - 2, -1, -1):
                rgt[j] = max(rgt[j + 1] - 1, points[i - 1][j])
            print(lft, rgt)
            for j in range(m):
                points[i][j] += max(lft[j], rgt[j])
        return max(points[-1])
