"""
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        # print(nums)
        diff_list = []
        for i in range(1, len(nums)):
            diff_list.append(nums[i] - nums[i-1])
        total = sum(diff_list)
        res = total
        length = len(diff_list)
        # print(diff_list)
        for left in range(4):
            right = length - 3 + left
            # print(left, right)
            # print(sum(diff_list[:left]), sum(diff_list[right:]), total - sum(diff_list[:left]) - sum(diff_list[right:]))
            res = min(res, total - sum(diff_list[:left]) - sum(diff_list[right:]))
        return res


S = Solution()
nums = [5,3,2,4]
print(S.minDifference(nums))
nums = [1,5,0,10,14]
print(S.minDifference(nums))
nums = [6,6,0,1,1,4,6]
print(S.minDifference(nums))
nums = [1,5,6,14,15]
print(S.minDifference(nums))
nums = [20,66,68,57,45,18,42,34,37,58]
print(S.minDifference(nums))
nums = [82,81,95,75,20]
print(S.minDifference(nums))