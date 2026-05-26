class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        curr = 0
        def backtrack(i, curr):
            if i == len(nums) or curr > target:
                return
            
            if curr == target:
                res.append(sol.copy())
                return
            
            backtrack(i+1, curr)
            
            sol.append(nums[i])
            
            backtrack(i, curr+nums[i])
            
            sol.pop()
            
        
        backtrack(0, curr)

        return res