"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
import math
class Solution:
    def productExceptSelf(self, nums):
        """
        can not deal with 0 and negative numbers
        """
        lg_sum = sum([math.log(n) if n != 0 else 0 for n in nums])
        # print([math.log(n) for n in nums])
        return [round(math.exp(lg_sum-math.log(n))) if n != 0 else 0 for n in nums ]


class Solution:
    def productExceptSelf(self, nums):
        """
        record left and right product to n in nums, then multiply them
        """
        res = [1]*len(nums)
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*tmp 
            tmp = tmp * nums[i]
        return res

class Solution:
    def productExceptSelf(self, nums):
        len_n = len(nums)
        left = [1]*len_n
        right  = [1]*len_n
        res = [1]*len_n
        for i in range(1,len_n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len_n-1, 0, -1):
            right[i-1] = right[i]*nums[i]
        for i in range(len_n):
            res[i] = left[i]*right[i]
        # print(left)
        # print(right)
        return res 

s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))

nums = [0,0]
print(s.productExceptSelf(nums))