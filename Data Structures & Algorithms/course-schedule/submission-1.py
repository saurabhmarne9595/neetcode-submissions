class Node:
    def __init__(self, val):
        val = val
        children = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        added = {i:[] for i in range(numCourses)}
        for cur, pre in prerequisites:
            if not cur in added:
                added[cur] = []
            added[cur].append(pre)
        visiting = set()
        def dfs(cur):
            if cur in visiting:
                return False
            if added[cur] == []:
                return True
            visiting.add(cur)
            for n in added[cur]:
                if not dfs(n):
                    return False
            visiting.remove(cur)
            added[cur] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True