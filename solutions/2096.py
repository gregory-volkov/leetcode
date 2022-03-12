# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, val, path):
            if node.val != val:
                left_path, right_path = None, None
                if node.left is not None: 
                    left_path = dfs(node.left, val, path + "L")
                if node.right is not None:
                    right_path = dfs(node.right, val, path + "R")
                if right_path is not None:
                    return right_path
                else:
                    return left_path
        
        def bfs(nodes2path, val):
            new_nodes2path = {}
            for node, path in nodes2path.items():
                if node.val == val:
                    return path
                if node.left is not None:
                    new_nodes2path[node.left] = path + "L"
                if node.right is not None:
                    new_nodes2path[node.right] = path + "R"
            return new_nodes2path
                
        
        nodes2paths = {root: ""}
        while isinstance(nodes2paths, dict):
            nodes2paths = bfs(nodes2paths, startValue)
        
        start_path = nodes2paths
            
        nodes2paths = {root: ""}
        while isinstance(nodes2paths, dict):
            nodes2paths = bfs(nodes2paths, destValue)
        
        dest_path = nodes2paths 
        
        i = 0
        while i < min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]:
            i += 1
        
        u_count = len(start_path) - i
        return "U" * u_count + dest_path[i:]
