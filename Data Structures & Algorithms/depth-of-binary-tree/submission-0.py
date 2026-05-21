# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth =  0
        def dfs(node, curr):
            if node:
                r = dfs(node.right, curr+1)
                l = dfs(node.left,curr+1)
                return max(l, r)
            return curr
        return dfs(root, depth)