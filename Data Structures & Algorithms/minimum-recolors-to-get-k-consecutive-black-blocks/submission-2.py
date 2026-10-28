class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, countW = k, 0 

        l,r = 0,0 
        while r < len(blocks):
            if blocks[r] =="W":
                countW += 1 
                # r += 1 
            if r-l+1 > k:
                if blocks[l] == "W":
                    countW -= 1 
                l += 1
            if r-l+1 == k:
                res = min(res, countW)
           
            r += 1 
        return res


