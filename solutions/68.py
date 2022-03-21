# 68. Text Justification
# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        ans = []
        while i < len(words):
            j = i + 1
            if j >= len(words): 
                last_line = True
            else:
                last_line = False
            cur_len = len(words[i])
            while j < len(words) and cur_len + len(words[j]) + 1 <= maxWidth:
                cur_len += len(words[j]) + 1
                j+= 1
                if j >= len(words):
                    last_line = True
                    break
            sum_len = sum(len(s) for s in words[i:j])
            extra = maxWidth - sum_len
            spaces_amt = j - i - 1
            spaces_amt = spaces_amt if spaces_amt > 0 else 1
            base_amt = extra // spaces_amt
            bonus_amt = extra - base_amt * spaces_amt
            
            if last_line:
                if j - i == 1:
                    buff = words[i]
                    buff += " " * base_amt
                else:
                    buff = " ".join(words[i:j])
                    buff += " " * (extra - spaces_amt)
            else:
                buff = words[i]
                if j - i == 1:
                    buff += " " * base_amt
                for k in range(1, j - i):
                    buff += " " * base_amt
                    buff += " " if k <= bonus_amt else ""
                    buff += words[i+k]
            
            ans.append(buff)
            i = j
        return ans
