# Problem: 704. Binary Search
# Runtime: 0 ms (Beats 100.00%)
# Memory: 13.2 MB (Beats 72.45%)

class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1 
        return -1       