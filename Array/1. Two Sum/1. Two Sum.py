# Problem: 1. Two Sum
# Runtime: 3 ms (Beats 54.31%)
# Memory: 13 MB (Beats 82.39%)

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i