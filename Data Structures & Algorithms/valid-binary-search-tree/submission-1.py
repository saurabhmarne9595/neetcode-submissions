# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = -float("inf")
        right = float("inf")
        def dfsRange(node, left, right):
            if not node:
                return True
            elif node.val > left and node.val < right:
                return (dfsRange(node.left, left, node.val) and
                dfsRange(node.right, node.val, right))
    
            else:
                return False
        return dfsRange(root, left, right)


