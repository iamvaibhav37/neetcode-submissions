class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def dfs(i, curr, pick):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for i in range(len(nums)):
                if pick[i] == False:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(i+1, curr, pick)
                    curr.pop()
                    pick[i] = False
        dfs(0, [], [False]*len(nums))

        return res


            
            