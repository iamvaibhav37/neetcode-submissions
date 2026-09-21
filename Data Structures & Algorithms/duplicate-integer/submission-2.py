class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count = {}
        # for n in nums:
        #     if n in count:
        #         return True
        #     count[n] = 1
        # return False

        arr = set(nums)
        if len(arr) == len(nums):
            return False
        else:
            return True

