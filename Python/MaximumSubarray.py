"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
"""
Thoughts:
iterate through the nums, 
set:
max_sum_nums = sum_nums = start = nums[0]
then add num to sum_nums, if it is larger than max_sum_nums, then max_sum_nums = sum_nums
if a num is larger than the sum_nums, it is the start
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums[0]
        max_sum_nums = nums[0]
        sum_nums = nums[0]
        for num in nums[1:]:
            sum_nums += num
            # print(num)
            if num > sum_nums:
                sum_nums = num
            if sum_nums > max_sum_nums:
                max_sum_nums = sum_nums
        return max_sum_nums

s = Solution()
test = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(test))