"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
 

Note:

The n will be in the range [1, 1000].
"""

from math import sqrt
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        sqrt_n = int(sqrt(n))+2
        res = n #copy one, paset n-1 times
        for i in range(2,sqrt_n):
            if n % i == 0:
                res = min(res, self.minSteps(n//i)+i)
        return res

class Solution:
    def minSteps(self, n: int) -> int:
        d = 2
        res = 0
        while n > 1:
            while n % d == 0:
                res += d #copy 1, paste d-1
                n = n//d
            d += 1
            # res += 1
        return res

S = Solution()
for n in range(1,10):
    print(n,S.minSteps(n))