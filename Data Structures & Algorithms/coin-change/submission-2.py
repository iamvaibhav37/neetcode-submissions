class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * ((amount)+1)
        
        
        def func(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if dp[amount] != -1:
                return dp[amount]
            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1 + func(amount-coin))          
            dp[amount] = ans 
            return dp[amount]

        ans = func(amount)

        if ans != float("inf"):
            return ans 
        else:
            return -1 
    

