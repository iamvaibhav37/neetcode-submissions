class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {} 
        res = -1
        for n in arr:
            dict[n] = dict.get(n, 0)+1 
        for n in arr:
            if dict[n] == n:
                res = max(res, n)
           
        return res