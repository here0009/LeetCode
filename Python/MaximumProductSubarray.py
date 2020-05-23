"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution_1:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Thoughts: keep record of start_to_first_minus_number and last_minus_number_to_end, the maximum product subarray is total or total/start_to_first_minus or total/last_minus_to_end
        Wrong: because 0
        """
        if len(nums) == 1:
            return nums[0]
        total = 1
        start_to_first_minus = 1
        last_minus_to_end = 1
        for num in nums:
            start_to_first_minus *= num
            if num < 0:
                break
        for num in nums[::-1]:
            last_minus_to_end *= num
            if num < 0:
                break
        for num in nums:
            total *= num
        return int(max(total, total/start_to_first_minus, total/last_minus_to_end))

class Solution_2:
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        Thoughts: 
        """
        B = A[::-1]
        print(A)
        print(B)
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        print(A)
        print(B)
        print(A+B)
        return max(A+B)


class Solution_3:
    def maxProduct(self, A):
        """
        If there is no 0s in nums.
        If the number of minus nums is even, the result is the total product, can be reached from start and end of nums.
        If the number of minus nums is odd, the result can be reached from start or end of nums, split by a minus num.
        Then we can add 0s to the nums, just restart the process, set the product to itself when encounters 0.
        """
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Thoughts: 
        """
        product = 1
        res = nums[0]
        for num in nums:
            product *= num
            res = max(product, res)
            if num == 0:
                product = 1
        product = 1
        for num in nums[::-1]:
            product *= num
            res = max(product, res)
            if num == 0:
                product = 1
        return res



s = Solution()
nums = [2,3,-2,4]
print(s.maxProduct(nums))
nums = [-2,0,-1]
print(s.maxProduct(nums))
nums = [-1,2]
print(s.maxProduct(nums))
nums = [-10]
print(s.maxProduct(nums))
nums = [0,2]
print(s.maxProduct(nums))
nums = [1,2,3,0,5,6,-9,2,-3,8]
print(s.maxProduct(nums))