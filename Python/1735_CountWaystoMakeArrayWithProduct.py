"""
You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.

Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.

 

Example 1:

Input: queries = [[2,6],[5,1],[73,660]]
Output: [4,1,50734910]
Explanation: Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.
Example 2:

Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: [1,2,3,10,5]
 

Constraints:

1 <= queries.length <= 104
1 <= ni, ki <= 104
"""


from typing import List
from functools import lru_cache
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        @lru_cache(None)
        def dp(n, k):
            print(n, k)
            if k == 1 or n == 1:
                return 1
            i = 1
            res = 0
            while i * i <= n:
                q, rmd = divmod(n, i)
                if rmd == 0:
                    for j in range(1, k):
                        res += dp(i, j) * dp(q, k - j)
                i += 1
            return res % M

        M = 10**9 + 7
        res = []
        for n, k in queries:
            res.append(dp(n, k))
        return res

# https://leetcode-cn.com/problems/count-ways-to-make-array-with-product/solution/yi-kan-jiu-dong-cha-ban-fa-jie-jue-you-z-9kr8/
from typing import List
from math import comb
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        """
        Thoughts:
        首先找出k的所有质数， 则k可以表示成为sum of(a_1**p_1, a_2**p_2, .... , a_n**p_n)
        对于每一组a，p, 可以构成n个数， 再构成k的方式等同于使用n-1个隔板分隔p个元素，元素可以位于隔板的同一/不同侧， 即为comb(n + p - 1, p)
        """
        def genPrimes(n):
            """
            generate primes less than n
            """
            primes = [2]
            for i in range(3, n + 1):
                for p in primes:
                    if i % p == 0:
                        break
                else:
                    primes.append(i)
            return primes

        def ways(n, k):
            """
            the ways of a_1*a_2*...*a_n = k
            """
            res = 1
            for p in primes:
                c = 0
                while k % p == 0:
                    k = k // p
                    c += 1
                if c > 0:
                    res *= comb(n + c - 1, c)
                if p > k:
                    break
            if k != 1:
                res *= n
            return res % M

        primes = genPrimes(100)
        # print(primes)
        M = 10**9 + 7
        res = []
        for n, k in queries:
            res.append(ways(n, k))
        return res

S = Solution()
queries = [[2,6],[5,1],[73,660]]
print(S.waysToFillArray(queries))
queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(S.waysToFillArray(queries))