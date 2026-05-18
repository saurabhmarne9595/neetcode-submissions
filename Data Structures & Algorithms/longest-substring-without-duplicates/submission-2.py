class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        length = 0
        left, right = 0, 0
        while right < len(s):
            
            if(s[right] not in visited):
                visited.add(s[right])
                right+=1    
            else:
                visited.remove(s[left])
                left+=1
            length = max(length, right-left)
            

        return length