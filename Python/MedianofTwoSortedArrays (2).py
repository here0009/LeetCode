"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from bisect import bisect
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def find(k,lo,hi):
            """
            find the k-th smallest element made by nums1 and nums2
            """
            while lo < hi:
                mid = (lo+hi)//2
                counts = bisect(nums1,mid) + bisect(nums2,mid)
                if counts < k:
                    lo = mid+1
                else:
                    hi = mid
            return lo
        
        l1,l2 = len(nums1),len(nums2)

        if l1 == 0:
            lo,hi = nums2[0],nums2[-1]
        elif l2 == 0:
            lo,hi = nums1[0],nums1[-1]
        else:
            lo,hi = min(nums1[0],nums2[0]), max(nums1[-1],nums2[-1])
        
        l3 = l1+l2
        if l3 % 2 == 1: #one median
            return find(l3//2+1,lo,hi)
        else:
            return (find(l3//2,lo,hi) + find(l3//2+1,lo,hi))/2

S = Solution()
nums1 = [1, 3]
nums2 = [2]
print(S.findMedianSortedArrays(nums1,nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(S.findMedianSortedArrays(nums1,nums2))

nums1 = []
nums2 = [1]
print(S.findMedianSortedArrays(nums1,nums2))