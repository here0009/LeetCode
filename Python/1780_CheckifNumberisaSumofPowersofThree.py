"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
"""


from math import log
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def dfs(idx, num):
            # print(idx, num)
            if num > n or idx > limit or self.res is True:
                return
            if num == n:
                self.res = True
            dfs(idx + 1, num)
            dfs(idx + 1, num + 3 ** idx)


        limit = int(log(n, 3)) + 1
        self.res = False
        dfs(0, 0)
        return self.res

S = Solution()
for i in [12, 91, 21]:
    print(i, S.checkPowersOfThree(i))
print(log(81, 3))
print(log(1E7, 3))