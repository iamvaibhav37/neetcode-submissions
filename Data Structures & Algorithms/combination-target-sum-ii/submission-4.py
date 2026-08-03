class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #in order to skip the same number if came across, i++

        def dfs(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or sum > target:
                return
            curr.append(candidates[i])
            dfs(i+1, curr, sum+candidates[i])
            curr.pop()
            while i+1 <len(candidates) and candidates[i]==candidates[i+1]:
                i += 1
            dfs(i+1, curr, sum)
        dfs(0, [], 0)
        return res 
