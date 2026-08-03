class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def F(i):
            if i>= len(nums):
                res.append((subset.copy()))
                return   #thourough explanation in 1 pages of superminds rough notebook/
            subset.append(nums[i])
            F(i+1)
            subset.pop()
            F(i+1)

        F(0)
        return res