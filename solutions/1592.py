# https://leetcode.com/problems/rearrange-spaces-between-words/
# 1592. Rearrange Spaces Between Words

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split(" ")
        words = [word for word in words if len(word) > 0]
        wrd_amt = len(words)
        space_amt = text.count(" ")
        if wrd_amt == 1:
            return words[0] + " " * space_amt
        sep = " " * (space_amt // (wrd_amt - 1))
        extra = " " * (space_amt % (wrd_amt - 1))
        
        return sep.join(words) + extra
