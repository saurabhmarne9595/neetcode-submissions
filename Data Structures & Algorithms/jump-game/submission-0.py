class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n):
            if  i > farthest:
                return False
            farthest = max(nums[i] +i, farthest)
            print(i, nums[i], farthest)
            # farthest-=1
        return True