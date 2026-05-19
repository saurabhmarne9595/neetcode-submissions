class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" 
        res, resLen = [-1,-1], float("inf")

        target, current = {}, {}
        for ch in t:
            target[ch] = 1+ target.get(ch, 0)
        
        has, need = 0, len(target)
        L=0
        for r in range(len(s)):
            current[s[r]] = 1+ current.get(s[r], 0)
            if s[r] in target and current[s[r]] == target[s[r]]:
                has+=1
            while has == need:
                if (r - L + 1) < resLen:
                    res = [L, r]
                    resLen = (r-L+1)
                current[s[L]]-=1
                if s[L] in target and current[s[L]] < target[s[L]]:
                    has-=1
                L+=1
            
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""

