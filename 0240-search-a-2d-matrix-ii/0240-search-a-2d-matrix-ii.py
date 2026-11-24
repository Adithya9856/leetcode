class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        r=n-1
        c=0
        while (r>=0)and(c<m):
            curr=matrix[r][c]
            if curr==target:
                return True
            elif target<curr:
                r-=1
            else:
                c+=1
        return False