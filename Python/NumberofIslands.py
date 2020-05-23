"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid) -> int:
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def dfs(i,j):
            visited[i][j] = 1
            for _i,_j in directions:
                dx,dy = i+_i,j+_j
                if inRange(dx,dy) and not visited[dx][dy] and grid[dx][dy] == '1':
                    dfs(dx,dy)

        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        return res


s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(grid))
grid = ["11000","11000","00100","00011"]
print(s.numIslands(grid))
grid = ['111000']
print(s.numIslands(grid))
x