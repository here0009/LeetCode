"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums) -> int:
        # print(nums)
        length = len(nums)
        if length == 0:
            return 1
        # the min of 1st missing positive is 1, the max of 1st missing positive is length, it can not be length+1
        for i, v in enumerate(nums):
            if v <= 0:
                nums[i] = length + 1
        # print(nums)
        for i, v in enumerate(nums):
            v = abs(v)
            if v <= length:
                nums[v - 1] = -1 * (abs(nums[v - 1]))
                #nums[v-1]  is negative means there is v appears before

        # print(nums)
        for i,v in enumerate(nums):
            if v > 0:
                return i+1
        return length+1
        # print(nums)
# return



S = Solution()
nums = [1,2,0]
print(S.firstMissingPositive(nums))
nums = [3,4,-1,1]
print(S.firstMissingPositive(nums))
nums = [7,8,9,11,12]
print(S.firstMissingPositive(nums))
nums = []
print(S.firstMissingPositive(nums))
nums = [1]
print(S.firstMissingPositive(nums))