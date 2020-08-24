"""
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

 

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []
 

Constraints:

1 <= n <= 100
"""


class Solution:
    def simplifiedFractions(self, n: int):
        def gcd(m, n):
            while m % n != 0:
                m, n = n, m % n
            return n

        def simplified(numerator, denominator):
            k = gcd(denominator, numerator)
            return '{}/{}'.format(numerator//k, denominator//k) 

        res_set = set()
        for denominator in range(2, n+1):
            for numerator in range(1, denominator):
                res_set.add(simplified(numerator, denominator))
        return list(res_set)

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
        
S = Solution()
for i in range(1,5):
    print(i, S.simplifiedFractions(i))