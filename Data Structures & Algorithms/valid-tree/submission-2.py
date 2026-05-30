class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        added = {i:[] for i in range(n)}
        seen = set()
        
        for start, end in edges:
            added[start].append(end)
            added[end].append(start)
        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)

            for j in added[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(seen)