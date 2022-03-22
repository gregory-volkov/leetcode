# 777. Swap Adjacent in LR String
# https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        if start.replace("X", "") != end.replace("X", ""): return False
        
        n = len(start)
        # XXXR -> RXXX wrong
        start_r, end_r, start_l, end_l = [], [], [], []
        for i in range(n):
            if start[i] == "R":
                start_r.append(i)
            elif start[i] == "L":
                start_l.append(i)
            if end[i] == "R":
                end_r.append(i)
            elif end[i] == "L":
                end_l.append(i)
        
        return all(j >= i for i, j in zip(start_r, end_r)) and\
            all(j <= i for i, j in zip(start_l, end_l))
