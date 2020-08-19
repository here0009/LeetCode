"""
Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]

Note:

0 <= K < N <= L <= 100
"""


# https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution
from functools import lru_cache
from math import factorial
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def dp(n, l):
            if n == l or n == K + 1:
                return factorial(n)
            return dp(n-1, l-1) * n + dp(n, l-1)*(n-K)
        M = 10**9 + 7
        return dp(N,L) % M


from math import factorial
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0]*(L+1) for _ in range(N+1)]
        M = 10**9 + 7
        for i in range(K+1, N+1):
            for j in range(i, L+1):
                if i == j or i == K+1:
                    dp[i][j] = factorial(i)
                else:
                    dp[i][j] = dp[i-1][j-1]*i + dp[i][j-1]*(i-K)
        return dp[-1][-1] % M

S = Solution()
N = 3
L = 3
K = 1
print(S.numMusicPlaylists(N, L, K))
N = 2
L = 3
K = 0
print(S.numMusicPlaylists(N, L, K))
N = 2
L = 3
K = 1
print(S.numMusicPlaylists(N, L, K))
print(S.numMusicPlaylists(3, 4, 0))