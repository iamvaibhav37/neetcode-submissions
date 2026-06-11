class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =1, max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i]+mid-1)//mid 
                # hours += hours
            if hours <= h:
                res = min(mid, res)
                r = mid-1
            elif hours > h:
                l = mid+1 
        
        return res
                

        