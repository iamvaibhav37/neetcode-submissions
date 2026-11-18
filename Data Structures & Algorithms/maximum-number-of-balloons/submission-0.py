class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map1 = {} 
      
        for ch in text:
            map1[ch] = map1.get(ch, 0)+1 

        count = float("inf")
       
        for ch in "balon":
            req = 2 if ch in "lo" else 1 
            count = min(count, (map1.get(ch,0)//req))
        return count

            

        


