"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bomb-enemy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import lru_cache
class Solution:
    def maxKilledEnemies(self, grid) -> int:
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        @lru_cache(None)
        def dfs(i, j, d):
            # print(i,j,d)
            if not inRange(i,j) or grid[i][j] == 'W':
                return 0
            ni, nj = i+directions[d][0], j+directions[d][1]
            return (grid[i][j] == 'E') + dfs(ni, nj, d)

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '0':
                    res = max(res, sum(dfs(i,j,d) for d in range(4)))
        return res

S = Solution()
grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
print(S.maxKilledEnemies(grid))

