class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]

        for u, v, cost in times:
            adj_list[u].append((v, cost))

        minheap = [(0, k)]
        visited = set() 
        totalcost = 0 
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            totalcost = max(cost, totalcost)
            for nei, neiCost in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (cost+neiCost, nei))
        if len(visited)==n:
            return totalcost
        else:
            return -1 