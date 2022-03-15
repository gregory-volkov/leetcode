# 1048. Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

class Solution:
    class Node:
        def __init__(self, s):
            self.nodes = set()
            self.s = s
            self.str_set = set(s)
            
        def add_neigh(self, node):
            self.nodes.add(node)
        
        def is_pred(self, node):
            if len(self.s) - len(node.s) != 1:
                return False
            extra = self.str_set.difference(node.str_set)
            if len(extra) > 1:
                return False
            for i in range(len(self.s)):
                if self.s[:i] + self.s[i + 1:] == node.s:
                    return True
            return False
    
        def __repr__(self):
            return self.s
        
    def longestStrChain(self, words: List[str]) -> int:
        
        max_lvl = 16
        levels = [[] for _ in range(max_lvl + 1)]
        
        node2preds = {}
        for wrd in words:
            node = self.Node(wrd)
            levels[len(wrd)].append(node)
        
        for i in range(max_lvl, 0, -1):
            for wrd in levels[i]:
                node2preds[wrd] = []
                for wrd_pre in levels[i - 1]:
                    if wrd.is_pred(wrd_pre):
                        node2preds[wrd].append(wrd_pre)
        
        lvl = 16
        chains = set()
        while lvl != 0:
            new_chains = set()
            for chain in chains:
                new_chains.update((pred, chain[1] + 1) for pred in node2preds[chain[0]])
            new_chains.update((node, 1) for node in levels[lvl])
            chains.update(new_chains)
            lvl -= 1
        
        return max(chains, key=lambda x: x[1])[1]


        # A better solution
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        # return max(dp.values())
