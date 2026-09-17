class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost) 
        # dp[0] = cost[0]
        # dp[1]= cost[1] 
        n = len(cost)
        def func(i):
            if i < 0:
                return 0 
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(func(i-1), func(i-2))
            return dp[i]

        return min(func(n-1), func(n-2))