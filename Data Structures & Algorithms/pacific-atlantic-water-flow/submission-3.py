class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = deque(), deque()
        p_set, a_set = set(), set() 
        rows, cols = len(heights), len(heights[0])

        for c in range(cols):
            p_set.add((0,c))
            pac.append((0,c))
        for r in range(rows):
            p_set.add((r,0))
            pac.append((r,0))

        for c in range(cols):
            a_set.add((rows-1,c))
            atl.append((rows-1,c))
        for r in range(rows):
            a_set.add((r,cols-1))
            atl.append((r,cols-1))
        
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        def get_cord(que, seen):
            while que:
                r, c = que.popleft()
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc 
                    if 0<= nr <rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c] and (nr,nc) not in seen: 
                       seen.add((nr,nc))
                       que.append((nr,nc))
            return seen 
        p_cords = get_cord(pac, p_set)
        a_cords = get_cord(atl, a_set)
     
        return list(p_cords.intersection(a_cords))        



         

        
        

