# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                print(node.val)
                left = node.left
                right = node.right
                node.left = right
                node.right =left
                dfs(node.right)
                dfs(node.left)
        def bfs(node):
            stack = []
            if node:
                print(node.val)
                stack.append(node.left)
                stack.append(node.right)
            while stack:
                n = stack.pop()
                bfs(n)

            
        print("DFS")
        dfs(root)
        # print("BFS")
        # bfs(root)
        return root