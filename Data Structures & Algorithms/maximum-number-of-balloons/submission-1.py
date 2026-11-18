class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map1 = {} 
        map2 = {}
        for ch in text:
            map1[ch] = map1.get(ch, 0)+1 
        for ch in "balloon":
            map2[ch] = map2.get(ch,0)+1 

        res = len(text)
        for c in "balloon":
            res = min(res, map1.get(c,0)//map2.get(c,0))
        return res
       

            

        


