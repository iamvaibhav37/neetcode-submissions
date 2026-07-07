class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):

                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            res = [nums[i], nums[j], nums[k], nums[l]]

                            if res not in arr:
                                arr.append(res)
        return arr
#the general approach to this is get k-2 for loops and then convet it to 2 pointer soln. 
#so  the TC for this bcms O(n^(k-1))