from _heapq import heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
# we have used maxheap to solve this one
        for x, y in points:
            dist = x**2 + y**2
            maxheap.append([-dist, x, y])
        heapq.heapify(maxheap)
        while len(maxheap)> k:
            heapq.heappop(maxheap)
        return [[x,y] for _,x, y in maxheap] 
        

