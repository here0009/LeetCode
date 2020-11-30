"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        maye be try to find n+1 from 0
        """
        if n < 10:
            return n % 10
        d = 1
        while n - 9*d*10**(d-1) > 0:
            print('d', n, d, 9*d*10**(d-1))
            n -= 9*d*10**(d-1)
            d += 1

        g_size = d*10**(d-1)
        g, g_rmd = divmod(n, g_size)
        q, q_rmd = divmod(g_rmd, d)
        print(n, g_size, g, g_rmd, q, q_rmd)
        if q_rmd == 1:
            return g+1
        else:
            return self.findNthDigit(q-1)


class Solution:
    def findNthDigit(self, n: int) -> int:
        d = 1
        while n - 9*d*10**(d-1) > 0:
            n -= 9*d*10**(d-1)
            d += 1
        n -= 1
        num = 10**(d-1) + (n//d)
        # print(n, num, d)
        return str(num)[n%d]

class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        base number => number => digit
        """
        n -= 1  # start from 0, 10, 100, each group got value 1~9, 10~99, 100~999
        d = 1
        while n - 9*d*10**(d-1) > 0:
            n -= 9*d*10**(d-1)
            d += 1
        num = 10**(d-1) + n//d  # the base number is 10**(d-1), n//d is the group the number lies in
        return str(num)[n%d]  # n%d is the nth digit

# https://leetcode.com/problems/nth-digit/discuss/828924/Python3-O(logN)-solution
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits 
            n -= 9*base*digit
            digit += 1
            base *= 10 
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])


S = Solution()
print(S.findNthDigit(3))
print(S.findNthDigit(11))
print(S.findNthDigit(15))
print(S.findNthDigit(38))

print(S.findNthDigit(10000))
# Output
# 6
# Expected
# 7
