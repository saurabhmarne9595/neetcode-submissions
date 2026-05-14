class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            print(nums[i])
            ans[i] = pre
            pre=pre*nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] = ans[i] *postfix
            postfix=postfix*nums[i]

        return ans