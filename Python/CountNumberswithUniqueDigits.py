"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def counts(n):
            if n == 0:
                return 1
            if n > 11:
                return 0
            n -= 1
            total = 9
            j = 9
            while n > 0:
                total *= j
                j -= 1
                n -= 1
            return total
            
        res = 0
        for i in range(n+1):
            # print(counts(i))
            res += counts(i)
        return res

S = Solution()
for n in range(15):
    print(n,S.countNumbersWithUniqueDigits(n))