class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for a in nums: 
            res = a ^ res 
        return res