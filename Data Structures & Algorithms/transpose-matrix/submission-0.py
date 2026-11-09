class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS,COLUMNS=len(matrix),len(matrix[0])
        res=[[0]*ROWS for _ in range(COLUMNS)]
        for r in range(ROWS):
            for c in range(COLUMNS):
                res[c][r]=matrix[r][c]
        return res