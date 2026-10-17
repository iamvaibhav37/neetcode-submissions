class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for i in range((rows//2)):
            matrix[i],matrix[rows-1-i] = matrix[rows-1-i],matrix[i] 
#swwapping was theimportant part here. both the variables shd be handled in the same line of code.     
        for r in range(rows):
            for c in range(cols):
                if r<c:
                    matrix[r][c],matrix[c][r] = matrix[c][r], matrix[r][c]
        