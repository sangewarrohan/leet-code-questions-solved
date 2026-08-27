# Problem: 54. Spiral Matrix
# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.1 MB (Beats 99.19%)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr=[]
        m,n,r,c=0,0,len(matrix),len(matrix[0])
        while m<r and n<c:
            for i in range(n,c):
                arr.append(matrix[m][i])
            m+=1
            for i in range(m,r):
                arr.append(matrix[i][c-1])
            c-=1
            if m<r:
                for i in range(c-1,n-1,-1):
                    arr.append(matrix[r-1][i])
                r-=1
            if n<c:
                for i in range(r-1,m-1,-1):
                    arr.append(matrix[i][n])
                n+=1
        return arr