class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        # print(dp)

        for i in range(1, n+1):
            for w in wordDict:
                wordLen = len(w)
                # print(i, s[i-1:wordLen+i-1], w)
                if wordLen<=i and s[i-wordLen:i] == w and dp[i-wordLen]:
                    dp[i] = True
                    # pass
        # print(dp)
        return dp[len(s)]