class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}
        def dfs(i):
            if i > len(nums)-1:
                return 0
            if i in seen:
                return seen[i]
            seen[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return seen[i]
        return dfs(0)