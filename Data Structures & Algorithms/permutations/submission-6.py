class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        hash = set()

        def dfs(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] in hash:
                    continue 
                
                hash.add(nums[i])
                curr.append(nums[i])
                dfs(curr)
                curr.pop() 
                hash.remove(nums[i])
        dfs([])
        return res

            
            