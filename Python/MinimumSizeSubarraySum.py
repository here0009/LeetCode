"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
from bisect import bisect_left
from bisect import bisect_right
class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1,-1]
        l = bisect_left(nums, target)
        if l == len(nums):
            l -= 1
        r = bisect_right(nums, target)-1
        # print(l,r)
        l_num, r_num = nums[l], nums[r]
        if l_num != target:
            l = -1
        if r_num != target:
            r = -1
        return [l,r]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums, target))

nums = []
target = 0
print(s.searchRange(nums, target))

nums = [2,2]
target = 3
print(s.searchRange(nums, target))
