class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s =  set(nums)
        largest=0
        listSeq = {}
        for num in nums:
            if num-1 not in s:
                length = 0
                while(num+length in s):
                    length+=1
                largest = max(largest, length)

        return largest       