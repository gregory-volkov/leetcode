# 792. Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subseq(small, large):
            if len(small) > len(large):
                return False
            sm_i = 0
            for i in range(len(large)):
                if sm_i == len(small):
                    break
                if large[i] != small[sm_i]:
                    continue
                else:
                    sm_i += 1
            return sm_i == len(small)
        
        wrd2occ = {}
        for wrd in words:
            if wrd not in wrd2occ:
                wrd2occ[wrd] = 1
            else:
                wrd2occ[wrd] += 1
        ans = 0
        for wrd in wrd2occ:
            ans += wrd2occ[wrd] if is_subseq(wrd, s) else 0

        return ans
