class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = {i :[] for i in range(n)}  #each node has[cost, node]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2)+ abs(y2-y1)
                adj_list[i].append((cost, j))
                adj_list[j].append((cost, i))
        
        #Prim's Algo
        res = 0 
        visited = set() 
        minH = [[0,0]]
        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue 
            res += cost 
            visited.add(i)
            for neicost, nei in adj_list[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neicost, nei])
        return res 