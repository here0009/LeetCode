"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
class Solution_1:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print(nums)
        pivot = nums[0]
        start, end = 1, len(nums)-1
        if end == 0:
            return pivot
        while True:
            while nums[start] > pivot:
                start+=1
                if start == len(nums)-1:
                    break
            while nums[end] < pivot:
                end-=1
                if end == 0:
                    break
            if start >= end:
                break
            nums[start], nums[end] = nums[end], nums[start]
        nums[0], nums[end] = nums[end], nums[0]
        if start+1 == k:
            return nums[start]
        if start+1 > k:
            return self.findKthLargest(nums[:start-1], k)
        else:
            return self.findKthLargest(nums[start:],k-start)

class Solution_2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse = True)
        return nums[k-1]


import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        QuickSelect
        sort the list large to small
        """
        random.shuffle(nums)
        pivot = nums[0]
        start, end = 1, len(nums)-1
        while start < end:
            while nums[start] >= pivot:
                start += 1
            while nums[end] < pivot:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
        return nums

s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums,k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums,k))        
nums = [1,2]
k = 2
print(s.findKthLargest(nums,k))