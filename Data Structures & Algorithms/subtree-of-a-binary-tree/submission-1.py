# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        sub = []
        def dfs(node, ar):
            if node:
                dfs(node.right, ar)
                dfs(node.left, ar)
                ar.append(node.val)
            ar.append(None)

        dfs(subRoot, sub)
        
        def dfsE(node, ar):
            ans = []
            dfs(node, ans)
            if ans == sub:
                return True
            if node:
                return dfsE(node.right, ar) or dfsE(node.left, ar)
            else:
                return False
            
        return dfsE(root, sub) 
        

        