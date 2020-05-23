"""
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

 

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1
Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1
Example 3:

Input: nums = [3,6]
Output: false
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

"""
"""
Thoughts:
if there are two num, 1 is their gcd, then it is a good array
"""
class Solution:
    def isGoodArray(self, nums) -> bool:
        def gcd(m,n):
            while n > 0:
                r = m % n
                m, n = n, r
            return m

        pre = nums[0]
        if len(nums) == 1:
            return pre == 1
        # g == gcd
        for i in range(1,len(nums)):
            g = gcd(nums[i], pre)
            if g == 1:
                return True
            else:
                pre = g
        return False

s = Solution()

nums = [12,5,7,23]
print(s.isGoodArray(nums))

nums = [29,6,10]
print(s.isGoodArray(nums))

nums = [3,6]
print(s.isGoodArray(nums))


nums = [18,18,18,15,54,45,45,45]
print(s.isGoodArray(nums))

nums = [6,10,15]
print(s.isGoodArray(nums))