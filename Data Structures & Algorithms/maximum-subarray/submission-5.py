class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = -float('inf')
        curMax = -float('inf')
        for num in nums:
            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)
        return maxSum