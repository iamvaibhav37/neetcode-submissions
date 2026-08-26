class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pick, nonpick = 0, 0
        arr1 = nums[0: n-1]
        arr2 = nums[1: n]
        dp1 = [-1]*n
        dp2 = [-1]*n
        # res = 0

        def f(i, nums, dp):
            if i==0:  return nums[0]
            if i<0:   return 0
            if dp[i]!= -1: return dp[i]

            pick = nums[i] + f(i-2, nums, dp)
            nonpick = 0 + f(i-1, nums, dp)         
            dp[i] = max(pick, nonpick) 
            return dp[i]
        
        return max(f(len(arr1)-1, arr1, dp1), f(len(arr2)-1, arr2, dp2))
        