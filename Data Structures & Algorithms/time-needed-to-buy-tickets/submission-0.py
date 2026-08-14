class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i,t) for i,t in enumerate(tickets))
        time = 0

        while queue:
            i, t = queue.popleft()
            t -= 1
            time += 1
            if i==k and t==0:
                return time
            if t>0:
                queue.append((i,t))