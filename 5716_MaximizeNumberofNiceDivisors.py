"""
You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the following conditions:

The number of prime factors of n (not necessarily distinct) is at most primeFactors.
The number of nice divisors of n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example, if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not.
Return the number of nice divisors of n. Since that number can be too large, return it modulo 109 + 7.

Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The prime factors of a number n is a list of prime numbers such that their product equals n.


Example 1:

Input: primeFactors = 5
Output: 6
Explanation: 200 is a valid value of n.
It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors: [10,20,40,50,100,200].
There is not other value of n that has at most 5 prime factors and more nice divisors.
Example 2:

Input: primeFactors = 8
Output: 18


Constraints:

1 <= primeFactors <= 109
"""


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:

        def power(base, d):
            if d == 0:
                return 1
            half_d, rmd = divmod(d, 2)
            tmp = power(base, half_d)
            if rmd == 0:
                return tmp * tmp % M
            else:
                return tmp * tmp * base % M

        M = 10**9 + 7
        d, rmd = divmod(primeFactors, 3)
        if d == 0:
            return rmd
        if rmd == 0:
            return power(3, d) % M
        if rmd == 1:
            d -= 1
            rmd += 3
        return power(3, d) * rmd % M


S = Solution()
print(S.maxNiceDivisors(5))
print(S.maxNiceDivisors(8))
print(S.maxNiceDivisors(18))
print(S.maxNiceDivisors(2))
print(S.maxNiceDivisors(545918790))
print(S.maxNiceDivisors(64))
print(S.maxNiceDivisors(4))
# 输入：
# 18
# 输出：
# 0
# 预期：
# 729
