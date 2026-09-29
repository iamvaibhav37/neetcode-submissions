class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        best = 0 

        for p in prices:
         
            min_val =min(min_val, p) 
            
            best = max(best, p-min_val)
        return best