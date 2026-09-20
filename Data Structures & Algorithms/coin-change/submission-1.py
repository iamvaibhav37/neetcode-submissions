class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1) 

        def dfs(amount): 
            if amount == 0:
                return 0 
            if amount < 0: 
                return float("inf")
            if dp[amount] != -1:
                return dp[amount]
            
            ans = float("inf")
            for coin in coins: 
                result = dfs(amount-coin)
                if result != float("inf"): 
                    ans = min(ans, 1+ result)
            dp[amount] = ans
            return ans

        ans = dfs(amount)

        return -1 if ans == float("inf") else ans