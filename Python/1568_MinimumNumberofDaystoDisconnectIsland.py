"""
Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:



Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
Example 3:

Input: grid = [[1,0,1,0]]
Output: 0
Example 4:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
Example 5:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1.
"""


"""
The tricky part of this question is to notice that, you can disconnect any given island formation in at most 2 days (and you need to convince yourself that this is true).
Example: Imagine we have 30-by-30 array of all 1's. For the top left corner, just remove the one to the right and below. And you are done.

Day 0: Check islands at day 0, return 0 if you have less than or greater than one island.

Day 1: If not, try to add water at any given location, and check if that gives you a valid island formation.

Day 2: Else, just return 2!
"""

class Solution:
    def minDays(self, grid) -> int:
        def dfs(i,j):
            visited[i][j] = 1
            for di, dj in directions:
                tmpi, tmpj = i+di, j+dj
                if tmpi >= 0 and tmpi < m and tmpj >= 0 and tmpj < n:
                    if visited[tmpi][tmpj] == 0 and grid[tmpi][tmpj] == 1:
                        dfs(tmpi, tmpj)

        def countIslands():
            res = 0
            for i in range(m):
                for j in range(n):
                    if visited[i][j] == 0 and grid[i][j] == 1:
                        res += 1
                        dfs(i, j)
            return res

        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = countIslands()
        if islands != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = [[0]*n for _ in range(m)]
                    grid[i][j] = 0
                    islands = countIslands()
                    grid[i][j] = 1
                if islands != 1:
                    return 1
        return 2

S = Solution()
grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
print(S.minDays(grid))
grid = [[1,1]]
print(S.minDays(grid))
grid = [[1,0,1,0]]
print(S.minDays(grid))
grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
print(S.minDays(grid))
grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
print(S.minDays(grid))

