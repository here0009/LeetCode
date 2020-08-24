"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        index = len(n) % 3
        res = ''
        for i,v in enumerate(n):
            if i % 3 == index:
                res += '.'
            res += v
        if res[0] == '.':
            res = res[1:]
        return res

S = Solution()
n = 987
print(S.thousandSeparator(n))
n = 1234
print(S.thousandSeparator(n))
n = 123456789
print(S.thousandSeparator(n))
n = 0
print(S.thousandSeparator(n))