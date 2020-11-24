"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""


class Solution:
    def maximumGap(self, nums) -> int:
        length = len(nums)
        nums.sort()
        if length < 2:
            return 0
        return max([nums[i] - nums[i-1] for i in range(1, length)])


S = Solution()
nums = [3,6,9,1]
print(S.maximumGap(nums))

nums = [10]
print(S.maximumGap(nums))

nums = [100,3,2,1]
print(S.maximumGap(nums))