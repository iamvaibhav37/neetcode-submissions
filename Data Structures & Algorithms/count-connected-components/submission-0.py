class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Adj_list = {i:[] for i in range(n)}
        res = 0
        for a, b in edges:
            Adj_list[a].append(b)
            Adj_list[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in Adj_list[node]:
                dfs(i)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res+= 1 
        return res 
            
