# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque() 
        res = []
        q.append((root, 0))
        while q:
            n, i = q.popleft()
            if n:
                if(len(res)-1 < i):
                    res.append([])
                res[i].append(n.val)
                if(n):
                    q.append((n.left, i+1))
                    q.append((n.right, i+1))
            
        return res
        