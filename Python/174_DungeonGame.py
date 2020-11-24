"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3  3
-5  -10 1
10  30  -5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""


from typing import List
from functools import lru_cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i,j,h):
            h += dungeon[i][j]
            if h <= 0:
                return False
            if i == R-1 and j == C-1:
                return True
            if (i+1 < R and dfs(i+1, j, h)) or (j+1 < C and dfs(i, j+1, h)):
                return True
            return False

        R, C = len(dungeon), len(dungeon[0])
        right = 1 - sum([i for i in dungeon[0] if i < 0]) - sum([dungeon[i][-1] for i in range(1, R) if dungeon[i][-1] < 0])
        left = 1
        while left < right:
            mid = (left + right)//2
            # print(left, right, mid)
            if dfs(0, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        need = [float('inf')]*(C-1) + [1]
        for row in dungeon[::-1]:
            for j in range(C-1, -1, -1):
                need[j] = max(min(need[j:j+2])-row[j], 1)
        return need[0]


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        dp = [[float('inf')]*(C+1) for _ in range(R+1)] #dp[i][j] is the min health we need to have if we want to rescue the princess
        dp[R][C-1], dp[R-1][C] = 1, 1
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        # for row in dp:
        #     print(row)
        return dp[0][0]

S = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(S.calculateMinimumHP(dungeon))