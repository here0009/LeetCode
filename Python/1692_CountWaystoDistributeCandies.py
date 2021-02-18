"""
There are n unique candies (labeled 1 through n) and k bags. You are asked to distribute all the candies into the bags such that every bag has at least one candy.

There can be multiple ways to distribute the candies. Two ways are considered different if the candies in one bag in the first way are not all in the same bag in the second way. The order of the bags and the order of the candies within each bag do not matter.

For example, (1), (2,3) and (2), (1,3) are considered different because candies 2 and 3 in the bag (2,3) in the first way are not in the same bag in the second way (they are split between the bags (2) and (1,3)). However, (1), (2,3) and (3,2), (1) are considered the same because the candies in each bag are all in the same bags in both ways.

Given two integers, n and k, return the number of different ways to distribute the candies. As the answer may be too large, return it modulo 109 + 7.

 

Example 1:



Input: n = 3, k = 2
Output: 3
Explanation: You can distribute 3 candies into 2 bags in 3 ways:
(1), (2,3)
(1,2), (3)
(1,3), (2)
Example 2:

Input: n = 4, k = 2
Output: 7
Explanation: You can distribute 4 candies into 2 bags in 7 ways:
(1), (2,3,4)
(1,2), (3,4)
(1,3), (2,4)
(1,4), (2,3)
(1,2,3), (4)
(1,2,4), (3)
(1,3,4), (2)
Example 3:

Input: n = 20, k = 5
Output: 206085257
Explanation: You can distribute 20 candies into 5 bags in 1881780996 ways. 1881780996 modulo 109 + 7 = 206085257.
 

Constraints:

1 <= k <= n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-ways-to-distribute-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import lru_cache
class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        """
        Thoughts:
        all combination is k**n
        one empty bag is n*(k - 1)**n
        wrong answer

        """
        @lru_cache(None)
        def comb(m, n):
            """
            m > n, ways of choose n elments from m elments
            """
            # print(m, n)
            if n == 0:
                return m
            if m == n:
                return 1
            return comb(m - 1, n) + comb(m - 1, n - 1)

        @lru_cache(None)
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n - 1)


        K = k
        M = 10**9 + 7
        total = k**n
        while k > 1:
            total -= comb(K, k - 1) * (k - 1)**n // factorial(k - 1)
            k -= 1
        return total % M


from functools import lru_cache
class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        @lru_cache(None)
        def dp(candies, bags):
            if candies < bags or candies <= 0 or bags <= 0:
                return 0
            if candies == bags:
                return 1
            res = dp(candies - 1, bags - 1) + bags * dp(candies - 1, bags)
            return res % M

        M = 10**9 + 7
        return dp(n, k)

class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        M = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][i] = 1
            for j in range(i + 1, n + 1):
                dp[i][j] = (dp[i - 1][j - 1] + i * dp[i][j - 1]) % M
        return dp[-1][-1]



S = Solution()
n = 3
k = 2
print(S.waysToDistribute(n, k))
n = 4
k = 2
print(S.waysToDistribute(n, k))
n = 20
k = 5
print(S.waysToDistribute(n, k))
n = 949
k = 620
print(S.waysToDistribute(n, k))