# https://leetcode.com/problems/find-leaves-of-binary-tree/
# 366. Find Leaves of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 0 - left node, 1 - right node
        def dfs(node, parent, ch_type):
            if node.left is None and node.right is None:
                if parent is not None:
                    if ch_type == 0:
                        parent.left = None
                    else:
                        parent.right = None
                yield node.val
            if node.left is not None:
                yield from dfs(node.left, node, 0)
            if node.right is not None:
                yield from dfs(node.right, node, 1)
        
        buf = [None]
        ans = []
        while len(buf) != 0:
            buf = []
            if root.left is None and root.right is None:
                ans.append([root.val])
                break
            else:
                dfs_gen = dfs(root, None, None)    
                for val in dfs_gen:
                    buf.append(val)
            ans.append(buf)
            
        return ans
