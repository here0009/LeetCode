"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        #the maximumProduct is either max*second*third or max*min*second_min (if min and second min is minus number)
        return max(sort_nums[-1]*sort_nums[-2]*sort_nums[-3], sort_nums[-1]*sort_nums[0]*sort_nums[1])
s = Solution()
nums = [1,2,3]
print(s.maximumProduct(nums))
nums = [1,2,3,4]
print(s.maximumProduct(nums))