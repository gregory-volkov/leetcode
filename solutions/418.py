# 418. Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        sentence_len = sum(len(wrd) for wrd in sentence) + len(sentence) - 1
        if any(len(wrd) > cols for wrd in sentence): return 0
        n = len(sentence)
        cur_row = 0
        i = 0
        while cur_row < rows:
            cur_occ = 0
            cur_occ += len(sentence[i%n])
            i += 1
            # Fill untill we return to the first word:
            while (i % n != 0) and (cur_occ + len(sentence[i%n]) + 1 <= cols):
                cur_occ += len(sentence[i%n]) + 1
                i += 1
            cur_occ += 1
            # Try to put whole sentences on the row:
            # sentence_len*x + x - 1 <= cols
            # x(sentence_len + 1) <= cols + 1
            # x <= (cols+1)/(sentence_len+1)
            if i%n == 0:
                if cur_occ == 0:
                    x = (cols + 1) // (sentence_len + 1)
                else:
                    x = (cols - cur_occ) // (sentence_len + 1)
                cur_occ += x * sentence_len + x - 1
                i += x*n

            while cur_occ + len(sentence[i%n]) + 1 <= cols:
                cur_occ += len(sentence[i%n]) + 1
                i += 1
            cur_row+= 1 
        return i//n
