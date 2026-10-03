class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        prev = 0 
        count = 0 
        for i in range(len(position)):
            dist = target - position[i]
            time = dist / speed[i]
            stack.append((position[i], time))
        stack.sort(reverse= True)

        for i in range(len(stack)):
            curr = stack[i][1]
            if curr > prev:
                count += 1
                prev = curr 
        return count