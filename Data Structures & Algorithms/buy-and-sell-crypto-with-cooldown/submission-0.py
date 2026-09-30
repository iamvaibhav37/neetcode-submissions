class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]

        def func(i, buy):
            if i >= len(prices):
                return 0 
            if dp[i][buy] != -1:
                return dp[i][buy]
            if buy:
                pick = -prices[i] + func(i+1, 0)
                nonpick =      0  + func(i+1, 1)
            else:
                pick = prices[i] + func(i+2, 1)
                nonpick =   0    + func(i+1, 0)

            dp[i][buy] = max(pick, nonpick)
            return dp[i][buy]
        
        return func(0, 1)
            