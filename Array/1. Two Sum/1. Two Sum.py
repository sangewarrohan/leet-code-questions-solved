# Problem: 1. Two Sum
# Runtime: 0 ms (Beats 100.00%)
# Memory: 12.9 MB (Beats 82.39%)

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i