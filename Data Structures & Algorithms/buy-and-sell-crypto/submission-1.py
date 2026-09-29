class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        best = 0 

        for p in prices:
            if p < min_val:
                min_val = p 
            else:
                best = max(best, p-min_val)
        return best