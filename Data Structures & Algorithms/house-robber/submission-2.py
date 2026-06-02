class Solution:
    def rob(self, nums: List[int]) -> int:
        curMax = - float("inf")
        seen = {}
        def dfs(i):
            if i > len(nums)-1:
                return 0
            if i in seen:
                return seen[i]
            curMax = max(nums[i] + dfs(i+2), dfs(i+1))
            seen[i] = curMax
            return curMax
        return dfs(0)