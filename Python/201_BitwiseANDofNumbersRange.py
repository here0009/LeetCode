"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        wrong answer
        """
        M = 2147483647
        powerOf2 = {0}
        res = m
        i = 2
        while i <= M :
            powerOf2.add(i)
            i = i*2
        for i in range(m+1, n+1):
            if res in powerOf2:
                return res
            res = res & i
            # print(res,i)
        return res


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        TLE
        """
        # print(bin(m), bin(n))
        res = ((1 << 64) - 1)
        while m <= n and res != 0:
            if m == n:
                res = res & m
            else:
                res = res & m & n
            m += 1
            n -= 1
            print(bin(m), bin(n), bin(res))
        return res

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # print(bin(m), bin(n))

        while m + (m & -m) <= n: 
            # print(bin(m), bin(n), len(bin(m)), len(bin(n)))
            # keep the high bit and remove low bit
            m = m & (m + (m & -m))
            if m == 0:
                return 0
        # print(bin(m), bin(n))
        return m & n


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m + (m & -m) <= n and m != 0:
            m = m & (m + (m & -m))
        return m & n


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p = 0
        while m != n:
            p += 1
            m >>= 1
            n >>= 1
        return m << p


S = Solution()
print(S.rangeBitwiseAnd(5,7))

# print(S.rangeBitwiseAnd(0,1))

print(S.rangeBitwiseAnd(2,4))

print(S.rangeBitwiseAnd(0,2))


print(S.rangeBitwiseAnd(2,6))
# 2
# 6
print(S.rangeBitwiseAnd(600000000*2, 2147483645))


