#4. Median of Two Sorted Arrays https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        sum = l1 + l2
        i1 = 0
        i2 = 0
        k = 0
        if sum % 2 == 1:
            target = (sum - 1) / 2
            o = True
        else:
            target = sum /2
            o = False
        while True:
            if o == True and k > target:
                return prev
            if o == False and k == target:
                f = prev
            if o == False and k > target:
                return (f + prev) / 2
            if i1 < l1 and i2 < l2:
                if nums1[i1] <= nums2[i2]:
                    prev = nums1[i1]
                    i1 += 1
                    k += 1
                    continue
                if i2 < l2 and (nums1[i1] > nums2[i2] or i1 >= l1):
                    prev = nums2[i2]
                    i2 += 1
                    k += 1
                    continue
            if i1 < l1 and i2 >= l2:
                prev = nums1[i1]
                i1 += 1
                k += 1
                continue
            if i2 < l2 and i1 >= l1:
                prev = nums2[i2]
                i2 += 1
                k += 1
                continue

if __name__ == "__main__":
    s = Solution()
    g = s.findMedianSortedArrays([1,3],[2] )
    print(g)