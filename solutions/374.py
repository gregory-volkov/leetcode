# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        mid = (i + j) // 2
        last_guess = guess(mid)
        while last_guess != 0:
            if last_guess == -1:
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j) // 2
            last_guess = guess(mid)
        return mid
