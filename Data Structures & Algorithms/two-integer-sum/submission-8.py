class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, n in enumerate(nums):
            # temp[i] = target - n
            complement = target - n

            if complement in temp:
                return [temp[complement], i]
            temp[n] = i
        return []