"""
Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
 

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Note:

The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""


from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(n, k):
            max_rev = n*(n-1)//2
            if max_rev < k:
                res = 0
            elif max_rev == k:
                res = 1
            else:
                res = 0
                for i in range(min(n, k+1)):
                    res += dp(n-1, k-i)
            return res % M
        M = 10**9+7
        return dp(n, k)


# https://leetcode.com/problems/k-inverse-pairs-array/discuss/282586/Python-376ms-A-less-confusing-cumulative-sum-approach
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        Thoughts: 
        if we add a num to  a sequence (length n-1), we can generate at most n-1 inverse pair,
        at least 0 inverse pair
        so m(n, k) = m(n-1, k) + .... + m(n-1, k - min(k, n-1))
        """
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        M = 10**9 + 7
        for i in range(1, n + 1):
            cumSum = 0
            for j in range(k + 1):
                if j == 0:
                    cumSum += 1
                else:
                    cumSum += dp[i - 1][j]
                    if j >= i:  # j at at most generate i-1 inverse, so dp[i - 1][m], m should at least be j-i+1, so j-i is not qualified
                        cumSum -= dp[i - 1][j - i]
                    cumSum = cumSum % M
                dp[i][j] = cumSum
        # for row in dp:
        #     print(row)
        return dp[n][k]



S = Solution()
print(S.kInversePairs(3, 0))
print(S.kInversePairs(3, 1))
print(S.kInversePairs(2, 2))
print(S.kInversePairs(1000, 30))