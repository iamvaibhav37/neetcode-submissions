class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bfs(i, sum, curr):
            if sum == target:
                res.append(curr.copy())
                return   
            if i>= len(nums) or sum>target:
                return
            curr.append(nums[i])
            bfs(i, sum + nums[i], curr)
            curr.pop()
            bfs(i+1, sum, curr)
            return res 
        return bfs(0, 0, [])    
            


        