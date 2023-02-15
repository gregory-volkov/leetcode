# 2101. Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_affect(bomb1, bomb2):
            i1, j1, r1 = bomb1
            i2, j2, r2 = bomb2
            # print(bomb1, bomb2,  (i1 - i1)**2 + (j1 - j2)**2 <= r1**2)
            return (i1 - i2)**2 + (j1 - j2)**2 <= r1**2

        graph = {}
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j: continue
                if (is_affect(bombs[i], bombs[j])):
                    if not i in graph:
                        graph[i] = []
                    graph[i].append(j)

        best_node, best_visited = None, []
        for i in range(len(bombs)):
            visited = []
            queue = [i]
            while queue:
                cur = queue.pop()
                visited.append(cur)
                if cur in graph:
                    queue.extend(node for node in graph[cur] if node not in queue and node not in visited)
        
            if len(best_visited) < len(visited):
                best_node, best_visited = i, visited
        
        return len(best_visited)
