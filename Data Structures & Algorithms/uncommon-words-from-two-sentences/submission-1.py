class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split() 
        words = words1 + words2 
        map1 = {}
        for word in words: 
            map1[word] = map1.get(word, 0)+1 

        res = [] 
        for word in map1:
            if map1[word] == 1:
                res.append(word)
        return res
        

