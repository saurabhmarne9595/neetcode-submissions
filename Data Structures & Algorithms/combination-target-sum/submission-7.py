class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [] , []

        def dfs(i, currSum):
            if currSum == target:
                res.append(sol.copy())
                return
            if i == len(nums) or currSum > target:
                return

            dfs(i+1, currSum)
            sol.append(nums[i])

            dfs(i, currSum+nums[i])
            sol.pop()

        dfs(0, 0)
        return res