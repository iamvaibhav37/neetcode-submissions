class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, sum):
            if sum == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or sum > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, sum+nums[i]) #this handles the frequency of the same number for sum
            cur.pop()
            dfs(i+1, cur, sum)   #this handles the different diff number for the sum 
        dfs(0, [], 0)
        return res
