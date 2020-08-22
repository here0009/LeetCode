"""
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:

Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
 

Example 2:

Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
 

Example 3:

Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
 

Note:

The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
"""


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def convert(num, base):
            res = ''
            while num != 0:
                d, r = divmod(num, base)
                res += str(r) + '|'
                num = d
            return res[::-1]

        n = int(n)
        for base in range(2, n):
            print(base,convert(n, base))

# https://leetcode.com/problems/smallest-good-base/discuss/543924/python-greater97-detailed-explaination-with-tips.
# https://leetcode.com/problems/smallest-good-base/discuss/235817/Python-Math-O(log(N))
# https://leetcode.com/problems/smallest-good-base/discuss/96587/Python-solution-with-detailed-mathematical-explanation-and-derivation
import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))
        print(n, m_max)
        for m in range(m_max, 1, -1):
            k = int(n**(1/m))
            print(m, k)
            if k**(m+1)-1 == n*(k-1):
                return str(k)
        return str(n-1)

S = Solution()
n = "13"
print(S.smallestGoodBase(n))
n = "4681"
print(S.smallestGoodBase(n))
n = "1000000000000000000"
print(S.smallestGoodBase(n))
n = "31"
print(S.smallestGoodBase(n))