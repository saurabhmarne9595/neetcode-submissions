class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L < R:
            M = (L+R) //2
            if(nums[M] > nums[R]):
                L=M+1
            else:
                R=M
        
        smallest = L

        if smallest == 0:
            L, R = 0, len(nums)-1
        elif(target >= nums[0] and target <= nums[smallest-1]):
            L, R = 0, smallest-1
        else:
            L, R = smallest, len(nums)-1

        while L <= R:
            M = (L+R)//2
            if(nums[M] == target):
                return M
            elif nums[M] < target:
                L= M + 1
            else:
                R = M - 1

        return -1