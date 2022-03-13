# 833. Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # abcd
        # 0 -> a, 1 -> b, 2 -> c, 3 -> d
        # 0 -> eee, 1 -> b, 2 -> "", 3 -> ffff
        
        id2str = {i: s[i] for i in range(len(s))}
        for i in range(len(indices)):
            st = indices[i]
            source = sources[i]
            if s[st: st + len(source)] == source:
                target = targets[i]
                for j in range(st, st + len(source)):
                    id2str[j] = ""
                id2str[st] = target
        
        max_k = max(id2str.keys())
        return "".join(id2str[k] for k in range(max_k + 1))
