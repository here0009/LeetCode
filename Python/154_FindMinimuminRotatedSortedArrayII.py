"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            # print(left, right, nums[left], nums[right])
            while nums[left] == nums[right] and left < right:
                left += 1
            if nums[left] < nums[right]:
                return nums[left]
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[left]

# class Solution:
#     def findMin(self, nums) -> int:
#         left

s = Solution()
nums = [1,3,5]
print(s.findMin(nums))
nums = [2,2,2,0,1]
print(s.findMin(nums))
nums = [4,5,6,7,0,1,2]
print(s.findMin(nums))
nums = [3,1]
print(s.findMin(nums))
nums = [3,1,3]
print(s.findMin(nums))
nums = [3,3,1,3]
print(s.findMin(nums))
