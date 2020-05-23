"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \\       /     /     / \\     \
     3     2     1      1   3      2
    /     /       \\                \
   2     1         2                 3
"""
from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def calTrees(p,q):
            if p >= q:
                return 1
            res = 0
            for i in range(p,q):
                res += calTrees(p,i)*calTrees(i+1,q)
            return res

        return calTrees(1,n+1)


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0]*(n+1)
        res[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                res[i] += res[j]*res[i-j-1]
        return res[n]