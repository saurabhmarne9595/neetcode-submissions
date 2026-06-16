class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for sell in range(1, len(prices)):
            if(sell!= buy and prices[sell] > prices[buy]):
                profit = max(profit, prices[sell]-prices[buy])
            if(prices[sell] < prices[buy]):
                buy=sell

        return profit    



        