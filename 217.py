# 217. Contains Duplicate https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        g = {}
        for n in nums:
            if n in g:
                return True
            else:
                g[n] = True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
