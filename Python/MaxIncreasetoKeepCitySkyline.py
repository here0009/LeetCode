"""
for grid[i][j], it can be increased to min(gird[i][:], grid[:][j]), so it can keep the skyline.
if grid[i][j] is the max value of its row or column, its stay the same.
turn the gird into a numpy matrix, so it is to calculate the max of each row and column.
"""
"""
import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):

        # :type grid: List[List[int]]
        # :rtype: int

        grid = np.array(grid, dtype = int)
        N = len(grid)
        row_max = grid.max(axis = 1)        
        col_max = grid.max(axis = 0)
        grid_new = np.array([[0]*N]*N, dtype = int)
        for i in range(N):
            for j in range(N):
                grid_new[i][j] = min(row_max[i], col_max[j])

        return sum(sum(grid_new)) - sum(sum(grid))
"""

"""
we can also to iterate the matrix, and keep the largest value of each row and column in a list
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        sum_old_grid = sum([sum(g) for g in grid])
        row_max = [0]*N     
        col_max = [0]*N
        #grid_new = [[0]*N]*N
        #it is shallow copy, so the value will change to the last assigned value.
        for i in range(N):
            for j in range(N):
                if grid[i][j] > row_max[i]:
                    row_max[i] = grid[i][j]
                if grid[j][i] > col_max[i]:
                    col_max[i] = grid[j][i]

        # print(row_max)
        # print(col_max)

        for i in range(N):
            for j in range(N):
                grid[i][j] = min(row_max[i], col_max[j])
                # print(grid[i][j])

        sum_new_grid = sum([sum(g) for g in grid])
        return sum_new_grid - sum_old_grid


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
s = Solution()
print(s.maxIncreaseKeepingSkyline(grid))