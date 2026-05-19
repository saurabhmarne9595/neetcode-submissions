class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res= ""
        resLen = float("inf")
        L, R = 0, 0
        subset = {}
        curr_subset = {}
        for ch in t:
            subset[ch] = 1 + subset.get(ch, 0)
        print(subset)

        def isValid(curr_subset, subset):

            for ch in subset:
                if curr_subset.get(ch, 0) < subset[ch]:
                    return False

            return True
        while L <= R and R < len(s):
            curr_subset[s[R]] = 1 + curr_subset.get(s[R], 0)
            print(s[L], s[R], curr_subset, res)
            while(isValid(curr_subset, subset)):
                print("is subset")
                if len(s[L: R+1]) < resLen:
                    res = s[L: R+1]
                    resLen = len(res)
                curr_subset[s[L]] -= 1
                L +=1
            else:
                R+=1

        return res
