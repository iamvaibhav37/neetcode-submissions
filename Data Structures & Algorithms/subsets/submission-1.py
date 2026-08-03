class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def F(i):
            if i>= len(nums):
                res.append((subset.copy()))
                return
            subset.append(nums[i])
            F(i+1)
            subset.pop()
            F(i+1)

        F(0)
        return res