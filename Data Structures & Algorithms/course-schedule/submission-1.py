class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range((numCourses))]

        for u, v in prerequisites:
            adj_list[u].append(v)
        
        visited = 2 
        unvisited = 0 
        visiting = 1 
        dp = [unvisited] * (numCourses)

        def dfs(node):
            state = dp[node]
            if state == visited: return True
            elif state == visiting: return False 

            dp[node] = visiting
            for nei in adj_list[node]:
                if not dfs(nei): return False 
            
            dp[node] = visited 
            return True 
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True


