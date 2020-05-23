"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
"""
Thoughts:
if a 0 is connected to another 0 that is on border, then it can not form an island
"""
class Solution:
    def closedIsland(self, grid) -> int:
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def onBorder(i,j):
            return i == 0 or i == m-1 or j == 0 or j == n-1

        def dfs(i,j):
            visited[i][j] = 1
            if onBorder(i,j):
                island_flag[0] = False
            for dx,dy in directions:
                di,dj = i+dx, j+dy
                if inRange(di,dj) and not visited[di][dj] and grid[di][dj] == 0:
                    dfs(di,dj)

        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        res = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    island_flag = [True]
                    dfs(i,j)
                    if island_flag[0]:
                        res += 1
        return res

s = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(s.closedIsland(grid))

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
print(s.closedIsland(grid))

grid=[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
print(s.closedIsland(grid))
