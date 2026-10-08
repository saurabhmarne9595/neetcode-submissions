class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sup ="".join(sorted(s))
            if sup in res:
                res[sup].append(s)
            else:
                res[sup] = [s]
        result=[]
        for k in res:
            result.append(res[k])
        
        return result