class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        pick, nonpick = 0,0 

        def f(i, nums, dp):
            # pick, nonpick = 0, 0
            if i == 0:  return nums[0]
            if i <0:    return 0
            if dp[i] != -1 : return dp[i]

            pick = nums[i] + f(i-2, nums, dp)
            nonpick = 0 + f(i-1, nums, dp)
            dp[i] = max(pick, nonpick)
            return dp[i]

        return f(n-1, nums, dp)
         