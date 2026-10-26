class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        best =0 

        edges = {} 

        for row in wall:
            position = 0 

            for brick in row[:-1]:
                position += brick
                edges[position] = edges.get(position, 0)+ 1 
        
        return len(wall) - max(edges.values(), default=0)
        