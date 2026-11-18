class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        while i<= len(prices):
            for j in range(i+1, len(prices)):
                if prices[i]>= prices[j]:
                    prices[i] = prices[i]-prices[j]
                    break
            i += 1
        return prices
