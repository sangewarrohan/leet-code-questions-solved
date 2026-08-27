# Problem: 35. Search Insert Position
# Runtime: 0 ms (Beats 100.00%)
# Memory: 12.8 MB (Beats 66.24%)

class Solution(object):
    def searchInsert(self, nums, target):
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
        return  low