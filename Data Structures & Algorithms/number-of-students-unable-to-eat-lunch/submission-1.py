class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students) 
        stack = sandwiches[::-1]
        rotations = 0

        while queue and rotations<len(queue):
            # for i in range(len(queue)):
            if queue[0] == stack[-1]:
                stack.pop()
                queue.popleft() 
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1
        return len(queue)   

