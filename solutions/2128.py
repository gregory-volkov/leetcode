# 2128. Remove All Ones With Row and Column Flips
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row1, row1_inverted = grid[0], [1 - el for el in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != row1 and grid[i] != row1_inverted:
                return False
        return True
