"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            i = 0
            while dividend >= divisor << (i+1):
                i += 1
            res += 1 << i
            dividend -= divisor << i
        return min(max(-2**31, res if sign else -res), 2**31-1)

# https://leetcode.com/problems/divide-two-integers/discuss/427345/Python-24ms-beats-99-with-and-wo-bitwise-operators
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            q, tmp = 1, divisor
            while tmp << 1 <= dividend:
                tmp <<= 1
                q <<= 1
            res += q
            dividend -= tmp
        return min(max(-2**31, res if sign else -res), 2**31-1)




S = Solution()
dividend = 10
divisor = 3
print(S.divide(dividend, divisor))
dividend = 7
divisor = -3
print(S.divide(dividend, divisor))