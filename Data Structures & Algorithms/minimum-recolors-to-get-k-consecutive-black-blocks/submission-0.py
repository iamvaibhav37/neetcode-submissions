class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_W = 0
        res = k 
        l = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count_W += 1
            if r-l+1 == k:
                res = min(res, count_W)
                if blocks[l] == 'W':
                    count_W -= 1
                l += 1
        return res

