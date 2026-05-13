class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            sup ="".join(sorted(s))
            if sup in hashmap:
                hashmap[sup].append(s)
            else:
                hashmap[sup] = [s]
        res=[]
        for k in hashmap:
            res.append(hashmap[k])

        return res