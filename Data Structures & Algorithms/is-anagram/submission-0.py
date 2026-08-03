class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in hash1:
                hash1[ch] += 1
            else:
                hash1[ch] = 1

        for ch in t:
            if ch in hash2:
                hash2[ch] += 1
            else:
                hash2[ch] = 1
            

        return hash1==hash2