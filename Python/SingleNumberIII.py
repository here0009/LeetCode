"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution_1:
    def singleNumber(self, nums):
        set_nums = set(nums)
        target = 2*sum(set_nums) - sum(nums)
        # print(target)
        for num in set_nums:
            if target - num in set_nums:
                return [num, target-num]
        return []

from functools import reduce
class Solution:
    """
    Thoughts:
    x ^ x = 0 and x ^ 0 = x
    so if there is two same num in nums, it will vanish to 0. xor all num in nums, if there is only 1 unique num in nums, it will be the result. if there are two unique num in nums, say a, b, then xor = a ^ b.
    And we know that there is one bit in xor is 1, that a and b is different in that bit.
    we use xor & - xor to get that bit.
    then use that bit to seperate nums into to groups, then xor each group, get a and b.
    """
    def singleNumber(self, nums):
        xor = reduce(lambda x,y: x^y, nums)
        # print(xor)
        sep_bit = xor & -xor #the bit that a and b is different
        a, b = 0, 0 # 0 ^ x = x
        for num in nums:
            if num & sep_bit:
                a = a ^ num
            else:
                b = b ^ num
        return [a,b]

s = Solution()
nums = [1,2,1,3,2,5]
print(s.singleNumber(nums))

