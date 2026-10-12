class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
#this is brute force solution, catch was to use magazine as list to be able to remove
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                magazine.remove(c)
        return True