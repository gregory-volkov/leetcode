# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_pr = 10**4
        
        for price in prices:
            cur_prof = price - min_pr
            if cur_prof > max_prof:
                max_prof = cur_prof
            if price < min_pr:
                min_pr = price
        return max_prof
