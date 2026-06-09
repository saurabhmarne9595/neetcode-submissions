class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = nums[0]
        pre = 0
        suf = 0
        for i in range(n):
            if pre == 0:
                pre = 1    
            if suf == 0:
                suf = 1

            pre*=nums[i]
            suf*=nums[n-i-1]    
            maxx = max(pre, suf, maxx)
        return maxx