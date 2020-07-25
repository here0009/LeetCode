"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while left < right:
            mid = (left + right) //2
            # print(left, right, mid)
            for i in (left, right, mid):
                if nums[i] == target:
                    return i
            if nums[mid] > target:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1 
            elif nums[mid] < target:
                if nums[left] < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

S = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(S.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(S.search(nums, target))
nums = [1,0]
target = 1
print(S.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 5
print(S.search(nums, target))