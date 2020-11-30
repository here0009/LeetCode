"""
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
Note:

N  will be in range [1, 1000].
"""


class Solution:
    def numTilings(self, N: int) -> int:
        dp = [1]*(N + 1)
        if N >= 2:
            dp[2] = 2
        for i in range(3, N+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[-1]

class Solution:
    def numTilings(self, N: int) -> int:
        dp = [0]*(N+1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        if N < 4:
            return dp[N]
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]*2 + 2*(i%2 == 0)
        return dp[-1]

class Solution:
    def numTilings(self, N: int) -> int:
        dp = [1,1,2]
        M = 10**9 + 7
        if N <= 2:
            return dp[N]
        dp = dp + (N-2)*[0]
        for i in range(3, N+1):
            dp[i] = (2*dp[i-1] + dp[i-3]) % M
        return dp[-1]

        
class Solution:
    def numTilings(self, N):
        a, b, c = 0, 1, 1
        for i in range(N - 1): a, b, c = b, c, (c + c + a) % int(1e9 + 7)
        return c

S = Solution()
for i in range(1, 11):
    print(i, S.numTilings(i))

print(10, S.numTilings(10))
print(4, S.numTilings(4))
# Your input
# 10
# Output
# 4449
# Expected
# 1255