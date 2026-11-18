class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if round(num**0.5, 1) == num**0.5: return True
        else: return False