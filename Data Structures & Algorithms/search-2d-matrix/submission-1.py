class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLUMNS=len(matrix),len(matrix[0])
        top,bottom=0,ROWS-1
        while top<=bottom:
            middle=(top+bottom)//2
            if matrix[middle][-1]<target:
                top=middle+1
            elif matrix[middle][0]>target:
                bottom=middle-1
            else:
                break
        if not top<=bottom:
            return False
        
        l,r=0,COLUMNS-1
        while l<=r:
            m=l+(r-l)//2
            if matrix[middle][m]<target:
                l=m+1
            elif matrix[middle][m]>target:
                r=m-1
            else:
                return True
        return False