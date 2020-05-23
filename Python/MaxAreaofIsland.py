"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global visited_grid, row, col
        visited_grid = list()
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            visited_grid.append([])
            for j in range(col):
                visited_grid[i].append(0)
        for i in range(row):
            for j in range(col):
                # if grid[i][j] == 1 and visited_grid[i][j] == 0:
                tmp = self.expandGrid(grid, i, j)
                if tmp > res:
                    res = tmp
                    # print(res)
        return res
        # print(visited_grid)
    def expandGrid(self,grid,i,j):
        if i >= row or i < 0 or j >= col or j < 0 or grid[i][j] == 0 or visited_grid[i][j] == 1:
            return 0
        if grid[i][j] == 1:
            # print(i,j)
            visited_grid[i][j] = 1
            return 1 + self.expandGrid(grid, i+1, j) + self.expandGrid(grid, i, j+1) + self.expandGrid(grid, i-1, j) + self.expandGrid(grid, i, j-1)



s = Solution()
test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(test))
test = [[0,0,0,0,0,0,0,0]]
print(s.maxAreaOfIsland(test))
test = [[0]]
print(s.maxAreaOfIsland(test))
test = [[1]]
print(s.maxAreaOfIsland(test))
test = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.maxAreaOfIsland(test))

test = [[0,1],[1,1]]
print(s.maxAreaOfIsland(test))