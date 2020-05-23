"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
import pysnooper
class Solution:
    # @pysnooper.snoop('./pysnooper.log')
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[n+i] = nums1[i]

        print(nums1)
        i,j,k = n, 0, 0
        while i < m+n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i+= 1
            else:
                nums1[k] = nums2[j]
                j+= 1
            k += 1
        # print(i,j,k)
        if j < n:
            nums1[k:] = nums2[j:]
        print(nums1)

s = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(s.merge(nums1, m, nums2, n))

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
print(s.merge(nums1, m, nums2, n))