# Problem: 48. Rotate Image
# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.4 MB (Beats 28.81%)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        st,ed=0,n-1
        while st<ed:
            for i in range(n):
                matrix[i][st],matrix[i][ed]=matrix[i][ed],matrix[i][st]
            st+=1
            ed-=1
        