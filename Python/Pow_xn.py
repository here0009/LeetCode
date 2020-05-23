"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        TLE for the test case 0.00001, 2147483647
        """
        abs_n = abs(n)
        res = 1
        while abs_n > 0:
            res *= x
            abs_n -= 1
        return res if n > 0 else 1/res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

class Solution:
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x,-n)
        half = self.myPow(x,n//2)
        if n % 2 == 0:
            return half*half
        else:
            return x*half*half


S = Solution()
x = 2.00000
n = 10
print(S.myPow(x,n))
x = 2.10000
n = 3
print(S.myPow(x,n))
x = 2.00000
n = -2
print(S.myPow(x,n))
x = 0
n = 0
print(S.myPow(x,n))
x = 0.00001
n = 2147483647
print(S.myPow(x,n))
x = 2.00000
n = -2147483648
print(S.myPow(x,n))