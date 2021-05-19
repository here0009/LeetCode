"""
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.
Example 2:

Input: n = 5, k = 5
Output: 1
Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.
Example 3:

Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.
 

Constraints:

1 <= n <= 1000
1 <= k <= n
"""


from functools import lru_cache
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        wrong answer
        """

        @lru_cache(None)
        def factorial(i):
            # print(i)
            if i == 1:
                return 1
            if i <= 0:
                return 0
            return factorial(i - 1) * i

        def dfs(premax, idx, seen):
            # print(premax, idx, seen, self.res)
            if idx == n + 1 or seen > k or k - seen > n - idx:
                return
            if premax == n:
                if seen == k:
                    self.res += factorial(n - idx)
                return
            for j in range(1, n + 1):
                if visited[j] == 0:
                    visited[j] = 1
                    dfs(max(j, premax), idx + 1, seen + int(j > premax))
                visited[j] = 0

        visited = [0] * (n + 1)
        self.res = 0
        dfs(0, 0, 0)
        M = 10**9 + 7
        return self.res % M


from functools import lru_cache
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Thoughts:
        for comb(n, k), we can place the longest stick in the end, so the combination is comb(n - 1, k - 1)
        we can any other stick in the end, so it is definetly blocked by the longest one, we got n - 1 choices at the end, and each got comb(n - 1, k)
        so comb(n, k) = comb(n - 1, k - 1) + (n - 1) * comb(n - 1, k)
        """

        @lru_cache(None)
        def dp(n, k):
            if n == k:
                return 1
            if n == 0 or k == 0:
                return 0
            return dp(n - 1, k - 1) + (n - 1) * dp(n - 1, k)

        M = 10 ** 9 + 7
        return dp(n, k) % M


class Solution:
    @lru_cache(None)
    def rearrangeSticks(self, n, k, mod=10**9 + 7):
        if n == k: return 1
        if k == 0: return 0
        return (self.rearrangeSticks(n - 1, k - 1) + self.rearrangeSticks(n - 1, k) * (n - 1)) % mod



class Solution:

    def rearrangeSticks(self, n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        M = 10 ** 9 + 7
        for i in range(1, k + 1):
            dp[i][i] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k + 1)):
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % M
        return dp[n][k]


S = Solution()
# n = 3
# k = 2
# print(S.rearrangeSticks(n, k))
# n = 5
# k = 5
# print(S.rearrangeSticks(n, k))
n = 20
k = 11
print(S.rearrangeSticks(n, k))