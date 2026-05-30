class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        added = {i:[] for i in range(n)}
        seen = set()
        for a, b in edges:
            added[a].append(b)
            added[b].append(a)
        
        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for n in added[i]:
                dfs(n)

        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+= 1
        return res