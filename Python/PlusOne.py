"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits):
        num = 0
        len_d = len(digits)-1
        for i,d in enumerate(digits):
            num += 10**(len_d-i)*d
        num += 1
        # print(num)
        res = []
        while num > 0:
            num,d = divmod(num,10)
            res.append(d)
        return res[::-1]

s = Solution()
digits = [1,2,3]
print(s.plusOne(digits))
digits = [4,3,2,1]
print(s.plusOne(digits))
digits = [0]
print(s.plusOne(digits))