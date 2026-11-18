class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0 
        visited = set() 
        visited.add((x,y))
        for ch in path:
            if ch == "N": y+=1 
            elif ch == "S":  y -=1
            elif ch == "E":  x +=1
            elif ch == "W":  x -=1 
            if (x,y) in visited:
                return True 
            else: visited.add((x,y))
        return False