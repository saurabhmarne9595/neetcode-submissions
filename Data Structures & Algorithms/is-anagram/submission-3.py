class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = dict()
        hasht = dict()
        for i in s:
            if (i in hashs.keys()):
                hashs[i] += 1
            else:
                hashs[i] = 1
        
        for j in t:
            if (j in hasht.keys()):
                hasht[j] += 1
            else:
                hasht[j] = 1     

        return hasht == hashs