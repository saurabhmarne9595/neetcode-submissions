class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = "".join([char for char in s if char.isalnum()]).lower()
        l = len(snew)-1
        for r in range(len(snew)//2):
            if snew[r] != snew [l-r]:
                return False
        return True


        
