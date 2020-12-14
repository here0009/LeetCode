"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

 

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

 

Note:

The range of n is [1,8].
"""

# https://leetcode.com/problems/largest-palindrome-product/discuss/276101/Python3-Math-and-Non-math-solutions-with-detailed-explanation
from math import sqrt
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        a = 2
        M = 1337
        while a < 10**n:
            upper = 10**n - a
            lower = int(str(upper)[::-1])
            tmp = a**2 - 4*lower
            if tmp >= 0:
                sqrt_tmp = sqrt(tmp)
                if int(sqrt_tmp) == sqrt_tmp:
                    r1 = (a + sqrt_tmp) / 2
                    r2 = (a - sqrt_tmp) / 2
                    if (r2 == int(r1) and r2 > 0) or r1 == int(r1):
                        print((10**n - a) * 10**n + lower)
                        return ((10**n - a) * 10**n + lower) % M
            a += 1
        return None


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        M = 1337
        hi = 10**n - 1
        lo = 10**(n - 1)
        max_x = hi // 11 * 11
        maxNum = hi * hi
        maxUpper = maxNum // 10**n
        for upper in range(maxUpper, lo - 1, -1):
            num = int(str(upper) + str(upper)[::-1])
            for x in range(max_x, lo - 1, -11):
                q, rmd = divmod(num, x)
                if rmd == 0 and lo <= q <= hi:
                    return num % M
                if q > hi:
                    break

class Solution_1:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        hi = 10**n - 1
        lo = 10**(n-1)
        maxNum = hi*hi
        firstHalf = maxNum // (10**n)
        for first in range(firstHalf, lo-1, -1):
            second = str(first)[::-1]
            num = int(str(first) + second)
            y_hi = hi//11*11
            for y in range(y_hi, lo-1, -11):
                if num % y == 0 and lo <= num // y <= hi:
                    return num % 1337
                if num // y > hi:
                    break
S = Solution()
for i in range(1, 9):
    print(i, S.largestPalindrome(i))
