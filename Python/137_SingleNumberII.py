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
# https://leetcode.com/problems/single-number-ii/discuss/699889/Python-Bit-Manipulation-O(32n)-but-easy-exaplained
class Solution:
    def singleNumber(self, nums) -> int:
        single = 0
        for i in range(32): #the range of int is [-2**31 ~ 2**31)
            count = 0
            for num in nums:
                if num & (1 <<i):
                    count += 1
            if count % 3 == 1:
                single |= (1 << i)
        return single if single < (1<<31) else single - (1<<32)

# https://leetcode.com/problems/single-number-ii/discuss/43360/The-simplest-solution-ever-with-clear-explanation
class Solution:
    def singleNumber(self, nums):
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0

print(1<<32)
print((1<<31) - 1)
s = Solution()
nums = [2,2,3,2]
print(s.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))
nums = [0,1,0,1,0,1,-4]
print(s.singleNumber(nums))
