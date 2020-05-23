"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        n1,n2 = len(nums1), len(nums2)
        vi_1 = {nums1[i]:i for i in range(n1-1, -1,-1)} #1st apperance of v
        vi_2 = {nums2[i]:i for i in range(n2-1, -1,-1)}
        pass

class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        n1,n2 = len(nums1), len(nums2)
        i1,i2 = 0,0
        remove_num = n1+n2-k
        res = []
        #remove the smaller ones
        while i1 < n1 and i2 < n2: #append the smaller one
            print(res)
            if nums1[i1] <= nums2[i2]:
                num = nums1[i1]
                i1 += 1
            else:
                num = nums2[i2]
                i2 += 1
            while remove_num > 0 and res and num > res[-1]:
                remove_num -= 1
                res.pop()
            res.append(num)

        while i1 < n1:
            while remove_num > 0 and res and nums1[i1] > res[-1]:
                 remove_num -= 1
                 res.pop()
            res.append(nums1[i1])
            i1 += 1

        while i2 < n2:
            while remove_num > 0 and res and nums2[i2] > res[-1]:
                 remove_num -= 1
                 res.pop()
            res.append(nums2[i2])
            i2 += 1
        return res

from collections import deque
class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        """
        1. largest(nums,p) find the largest p number in nums1 and nums2 while keep the relative order
        2. find the max list of merge(largest(nums1,i) + largest(nums2, k-i) for i in ragne(k+1))
        """
        def largest(nums, p):
            res = []
            drop = len(nums)-p
            for n in nums:
                while res and drop > 0 and n > res[-1]:
                    res.pop()
                    drop -= 1
                res.append(n)
            # print(nums, p,res[:p])
            return deque(res[:p])

        # def merge(list1, list2): 
        # #compare the element is wrong, if two elment is the same, we should compare the rest of the list and decide which one to use.
        #     i1,i2 = 0,0
        #     l1,l2 = len(list1), len(list2)
        #     res = []
        #     while i1 < l1 and i2 < l2:
        #         if list1[i1] >= list2[i2]:
        #             res.append(list1[i1])
        #             i1 += 1
        #         else:
        #             res.append(list2[i2])
        #             i2 += 1
        #     res.extend(list1[i1:])
        #     res.extend(list2[i2:])
        #     return res

        def merge(list1, list2): 
        #compare the element is wrong, if two elment is the same, we should compare the rest of the list and decide which one to use.
            res = []
            while list1 and list2:
                if list1 > list2:
                    res.append(list1.popleft())
                else:
                    res.append(list2.popleft())
            res.extend(list1)
            res.extend(list2)
            return res

        length1 = len(nums1)
        length2 = len(nums2)

        return max(merge(largest(nums1,i),largest(nums2, k-i)) for i in range(k+1) if i <=length1 and k-i <= length2)
            

S = Solution()
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print(S.maxNumber(nums1, nums2, k))
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print(S.maxNumber(nums1, nums2, k))
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
print(S.maxNumber(nums1, nums2, k))

nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 15
print(S.maxNumber(nums1, nums2, k))
# Output
# [7,3,8,2,5,6,4,4,0,0,6,5,7,6,2]
# Expected
# [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]