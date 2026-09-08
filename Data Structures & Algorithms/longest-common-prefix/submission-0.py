class Trienode:
    def __init__(self):
        self.children = {}
        self.EndofWord  = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = Trienode()
        

        for word in strs:
            curr = self.root
            for c in word: 
                if c not in curr.children:
                    curr.children[c] = Trienode() 
                curr = curr.children[c]
            curr.EndofWord = True
        res = ""
        curr = self.root
        while len(curr.children)==1 and curr.EndofWord == False:
            for c in curr.children:
                res += c 
                curr = curr.children[c] 
        return res




            
