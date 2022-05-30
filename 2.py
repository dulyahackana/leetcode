#1. Two Sum https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        g = {}
        for i, n in enumerate(nums):
            if target - n in g:
                return [g[target - n], i]
            g[n] = i
