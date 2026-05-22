# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pTree = []
        qTree = []
        def dfs(node, ar):
            if node:
                dfs(node.right, ar)
                dfs(node.left, ar)
                ar.append(node.val)
            ar.append(None)

        dfs(p, pTree)
        dfs(q, qTree)
        return pTree == qTree