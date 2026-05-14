class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr <len(s):
            end = curr
            while s[end] != '#':
                end+= 1
            length = int(s[curr:end])
            res.append(s[end+1: end+length+1])
            curr = end + length + 1

        return res


