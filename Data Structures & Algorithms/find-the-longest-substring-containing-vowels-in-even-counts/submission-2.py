class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        mask = 00000
        mask_to_ind = {0: -1}
        res = 0

        for i,c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a')) 
            if mask in mask_to_ind:
                length = i - mask_to_ind[mask]
                res = max(res, length)
            else:
                mask_to_ind[mask] = i 
        return res

            


           
           
      