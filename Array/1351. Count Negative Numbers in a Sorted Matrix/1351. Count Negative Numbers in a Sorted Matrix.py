# Problem: 1351. Count Negative Numbers in a Sorted Matrix
# Runtime: 0 ms (Beats 100.00%)
# Memory: 13.1 MB (Beats 68.20%)

class Solution(object):
    def countNegatives(self, grid):
        r=len(grid)
        c=len(grid[0])
        count=0
        rp=r-1
        cp=0
        while rp>=0 and cp<c:
            if grid[rp][cp]<0:
                count=count+(c-cp)
                rp=rp-1
            else:
                cp=cp+1
        return count
