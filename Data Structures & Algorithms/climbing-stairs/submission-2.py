class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(target):
            if target <= 1:
                return 1

            if target in memo:
                return memo[target]

            memo[target] = dp(target - 1) + dp(target - 2)
            return memo[target]

        return dp(n)