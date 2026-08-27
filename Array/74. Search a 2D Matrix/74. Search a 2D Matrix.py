# Problem: 74. Search a 2D Matrix
# Runtime: 7 ms (Beats 0.40%)
# Memory: 12.5 MB (Beats 68.25%)

class Solution(object):
    def searchMatrix(self, matrix, target):
        r=len(matrix)
        c=len(matrix[0])
        low=0
        high=(r*c)-1
        while low<=high:
            mid=(low+high)//2
            rp=mid//c
            cp=mid%c
            print(low,high,mid,rp,cp)
            if matrix[rp][cp]==target:
                return True
            elif matrix[rp][cp]<=target:
                low=mid+1
            else:
                high=mid-1
        return False