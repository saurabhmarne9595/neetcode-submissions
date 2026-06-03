class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            seen = {}

            def dfs(i):
                if i >= len(arr):
                    return 0

                if i in seen:
                    return seen[i]

                seen[i] = max(arr[i] + dfs(i + 2), dfs(i + 1))
                return seen[i]

            return dfs(0)

        return max(helper(nums[1:]), helper(nums[:-1]))