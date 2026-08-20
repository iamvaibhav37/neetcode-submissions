class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        directions = ([1,0], [-1,0], [0,1], [0,-1])
        pacific, atlantic = set(), set()
#reverse approach, memoization, rather going fro each cell to the ocean, coming from the ocean is time effiecient. 
        def dfs(r, c, visited, prev_height):
            if (r,c) in visited:
                return
            if r<0 or c<0 or r>=row or c>=col:
                return
            if heights[r][c]< prev_height:
                return
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])
        
        for c in range(col):
            dfs(0, c, pacific, heights[0][c])
            dfs(row-1, c, atlantic, heights[row-1][c])
        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, col-1, atlantic, heights[r][col-1])
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res