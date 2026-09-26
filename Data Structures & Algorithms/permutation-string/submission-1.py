class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# from types import _ReturnT_co
        target = sorted(s1)
        n1, n2 = len(s1), len(s2)

        if n1> n2:
            return False
        for i in range(n2-n1+1):
            window = s2[i: i+n1]
            if sorted(window) == target:
                return True
        return False
        


        