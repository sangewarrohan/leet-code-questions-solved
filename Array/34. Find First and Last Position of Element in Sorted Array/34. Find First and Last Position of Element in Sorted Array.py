# Problem: 34. Find First and Last Position of Element in Sorted Array
# Runtime: 0 ms (Beats 100.00%)
# Memory: 13.1 MB (Beats 34.23%)

class Solution(object):
    def searchRange(self, nums, target):
        low=0
        high=len(nums)-1
        st=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                st=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(nums)-1
        end=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                end=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return [st,end]