class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        start = 0
        resLen =  0
        n = len(s)
        for i in range(n):
            # print("loop - ", i)
            left, right = i, i
            while left >= 0 and right < n and  s[left] == s[right]:
                # print(left, right, res)
                if resLen < (right - left + 1):
                    resLen = right - left + 1
                    start = left
                left-=1
                right+=1
                    
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                # print(left, right, res)
                if resLen < (right - left + 1):
                    resLen = right - left + 1
                    start = left
                left-=1
                right+=1
            
        return s[start: start+resLen]

        