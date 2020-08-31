"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def getMaxLen(self, nums) -> int:
        length = len(nums)
        # if length == 1:
        #     return int(nums[0] > 0)
        prePositive, preNegative = 0, length
        curr = 1
        res = 0
        # print(nums)
        for i,v in enumerate(nums):
            if v == 0:
                curr = 1
                prePositive, preNegative = i+1, length
                continue
            curr *= v
            if curr > 0:
                res = max(res, i - prePositive+1)
                # prePositive = min(i, prePositive)
            elif curr < 0:
                res = max(res, i - preNegative)
                preNegative = min(i, preNegative)
            # print(res, prePositive, preNegative)
        return res


class Solution:
    def getMaxLen(self, nums) -> int:
        pos, neg, res = 0, 0, 0 # record the currently longest pos and neg array at the specific index
        for num in nums:
            if num > 0:
                pos, neg = pos + 1, neg + 1 if neg else 0
            elif num < 0:
                pos, neg = neg + 1 if neg else 0, pos + 1
            else:
                pos, neg = 0, 0
            res = max(res, pos)
        return res

S = Solution()
nums = [1,-2,-3,4]
print(S.getMaxLen(nums))
nums = [0,1,-2,-3,-4]
print(S.getMaxLen(nums))
nums = [-1,-2,-3,0,1]
print(S.getMaxLen(nums))
nums = [-1,2]
print(S.getMaxLen(nums))
nums = [1,2,3,5,-6,4,0,10]
print(S.getMaxLen(nums))
nums = [1000000000]
print(S.getMaxLen(nums))
nums = [2,1]
print(S.getMaxLen(nums))
nums = [-1000000000,-1000000000]
print(S.getMaxLen(nums))
nums = [0,1,-2,-3,-4]
print(S.getMaxLen(nums))
nums = [-16,0,-5,2,2,-13,11,8]
print(S.getMaxLen(nums))