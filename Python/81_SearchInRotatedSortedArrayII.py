"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        wrong answer
        """
        left, right = 0, len(nums)-1
        while left <= right:
            print(nums[left:right+1])
            mid = (left + right)//2
            print(left, right, mid)
            if nums[mid] == target:
                return True
            if nums[left] <= target < nums[mid] or not(nums[mid] < target <= nums[right]):
                right = mid - 1
            else:
                left = mid + 1
            print(left, right, mid)
        return False

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            print(nums[left:right+1])
            mid = (left + right)//2
            print(left, right, mid)

            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            print(left, right, mid)
        return False


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def find(i, j):
            if i > j:
                return False
            if i == j:
                return nums[i] == target
            while j > i and nums[j] == nums[i]:
                j -= 1
            mid = (i+j)//2
            if nums[mid] == target:
                return True
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            return find(i, j)

        if not nums:
            return False
        return find(0, len(nums)-1)

S = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(S.search(nums, target))
nums = [2,5,6,0,0,1,2]
target = 3

print(S.search(nums, target))
nums = [3,1]
target = 1
print(S.search(nums, target))

nums = [1,3,1,1,1]
target = 3
print(S.search(nums, target))

nums = []
target = 5
print(S.search(nums, target))
nums = [1]
target = 0
print(S.search(nums, target))