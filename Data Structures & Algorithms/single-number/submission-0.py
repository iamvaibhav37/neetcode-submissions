class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = set()

        for n in nums:
            if n in hm:
                hm.remove(n)
            else:
                hm.add(n)
        return hm.pop()