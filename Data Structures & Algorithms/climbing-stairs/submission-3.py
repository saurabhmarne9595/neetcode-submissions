class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dp(target):
            if target in mem:
                return mem[target]
            if target == 0:
                return 1
            elif target == 1:
                return 1
                
            else:
                mem[target] = dp(target-1) + dp(target - 2) 
                return mem[target] 
        return dp(n) 