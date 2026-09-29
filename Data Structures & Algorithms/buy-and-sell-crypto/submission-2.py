class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_val = prices[0]
        best = 0 

        for i in range(1,len(prices)):
            min_val = min(prices[:i]) 
            best = max(best, prices[i]-min_val)
        return best           