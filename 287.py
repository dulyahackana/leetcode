#287. Find the Duplicate Number https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                return n
            else:
                d[n] = 1
