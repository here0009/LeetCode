"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
from functools import reduce
class Solution:
    def singleNumber(self, nums) -> int:
        xor = reduce(lambda x,y:x^y, nums)
        print(xor)
        print(bin(xor))
        for num in nums:
            print(bin(num))
        return

s = Solution()
nums = [2,2,3,2]
print(s.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))
