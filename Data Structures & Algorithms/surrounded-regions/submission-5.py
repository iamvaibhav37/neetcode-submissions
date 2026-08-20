class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        direction = ([1,0], [-1,0],[0,1], [0,-1])

        def convert(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!="O":
                return
            board[i][j] = "T"
            for dr, dc in direction:
                convert(i+dr, j+dc)
        
        
        for c in range(cols):
            if board[0][c]=="O":
                # board[0][c]="T"
                convert(0,c)
            if board[rows-1][c]=="O":
                # board[rows-1][c]="T"
                convert(rows-1,c)
                
        for r in range(rows):
            if board[r][0]=="O":
                # board[r][0]="T"
                convert(r,0)
            if board[r][cols-1]=="O":
                # board[r][cols-1]="T"
                convert(r,cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"
                

