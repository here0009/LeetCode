"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        sum_num = 0
        len_num = len(nums)
        for num in nums:
            sum_num += num
            max_num = max(num, max_num)
        # print(sum_num, max_num)
        if max_num < len_num: #max num is missing
            return max_num+1
        else: #there is max num, calculate the sum based on max num, then substract the real sum
            return int((max_num)*(max_num+1)/2 - sum_num)

s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums))
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))
nums = [1]
print(s.missingNumber(nums))
nums = [0]
print(s.missingNumber(nums))
nums = [0,1]
print(s.missingNumber(nums))