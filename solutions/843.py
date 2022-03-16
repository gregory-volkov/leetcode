# 843. Guess the Word
# https://leetcode.com/problems/guess-the-word/


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def get_var(lst):
            mean = sum(lst) / len(lst)
            return sum((el - mean) ** 2 for el in lst)
        
        def dist(s1, s2):
            return sum(1 if ch1 != ch2 else 0 for ch1, ch2 in zip(s1, s2))
        
        wrd_len = 6
        n = len(wordlist)
        dist_m = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                dist_m[i][j] = dist_m[j][i] = dist(wordlist[i], wordlist[j])
        
        dist_var = []
        for i in range(n):
            dist_var.append(get_var(dist_m[i]))
        
        fst_sus = max(range(n), key=lambda x: dist_var[x])
        guess = master.guess(wordlist[fst_sus])
        suss = [i for i in range(n) if dist_m[fst_sus][i] == wrd_len - guess]
        
        while len(suss) != 0 and guess != 6:
            new_sus = max(suss, key=lambda x: dist_var[x])
            guess = master.guess(wordlist[new_sus])
            suss = [i for i in suss if dist_m[new_sus][i] == wrd_len - guess]
        
