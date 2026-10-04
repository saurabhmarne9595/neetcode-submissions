class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for char in s:
            if char in dicS.keys():
                dicS[char]+= 1
            else:
                dicS[char]= 1
        for char in t:
            if char in dicT.keys():
                dicT[char]+= 1
            else:
                dicT[char]= 1

        return dicT == dicS
