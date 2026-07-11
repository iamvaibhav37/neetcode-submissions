class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#this uses max heap see how we negating values to get the reverse answerws
#also at the end return '-' is being used to get final positive answer
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)> 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y-x))
        
        return -heap[0] if heap else 0