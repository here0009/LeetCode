"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #there is a n*5, and there must be at least one n*2 before it, so there is one trailing zero. for n*25, n*25*4 = n*100, so two traing zero for 25*n 
        counts = 0
        d = 5
        while d <= n:
            counts += n//d
            d = 5*d
        return counts 


class Solution:
    def trailingZeroes(self, n: int) -> int:
        def f(n):
            if n < 5:
                return 0
            return n//5 + f(n//5)
        return f(n)

S = Solution()
n = 3
print(S.trailingZeroes(n))

n = 5
print(S.trailingZeroes(n))

n = 100
print(S.trailingZeroes(n))
