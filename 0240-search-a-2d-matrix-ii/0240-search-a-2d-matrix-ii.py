class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowlen,collen=len(matrix),len(matrix[0])
        row=0
        col=collen-1
        while (row<rowlen) and (col>=0):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False