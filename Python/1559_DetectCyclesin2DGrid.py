"""
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid consists only of lowercase English letters.
"""


class Solution:
    def containsCycle(self, grid) -> bool:
        def inRange(i,j):
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(prei, prej,i,j,v):
            visited[i][j] += 1
            if visited[i][j] >= 2:
                return
            for di,dj in directions:
                tmpi, tmpj = i+di, j+dj
                if inRange(tmpi, tmpj) and grid[tmpi][tmpj] == v and (tmpi, tmpj) != (prei, prej):
                    dfs(i,j,tmpi,tmpj,v)

        m, n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),[-1,0]]
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    dfs(-1,-1,i,j,grid[i][j])
        for row in grid:
            print(row)
        for row in visited:
            print(row)
        max_v = max(max(row) for row in visited)
        return max_v >= 2


class Solution:
    def containsCycle(self, grid) -> bool:
        def inRange(i,j):
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(prei, prej,i,j,v):
            if self.res or visited[i][j] == 1:
                self.res = True
                return
            visited[i][j] = 1
            for di,dj in directions:
                tmpi, tmpj = i+di, j+dj
                if inRange(tmpi, tmpj) and grid[tmpi][tmpj] == v and (tmpi, tmpj) != (prei, prej):
                    dfs(i,j,tmpi,tmpj,v)

        m, n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),[-1,0]]
        visited = [[0]*n for _ in range(m)]
        self.res = False
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    dfs(-1,-1,i,j,grid[i][j])
        # for row in visited:
        #     print(row)
        return self.res

S = Solution()
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
print(S.containsCycle(grid))
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
print(S.containsCycle(grid))
grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
print(S.containsCycle(grid))