class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                return nums[i]
            else:
                hm[nums[i]] = i 