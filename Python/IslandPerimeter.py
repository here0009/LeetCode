"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        if row == 0 or col == 0:
            return 0
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    res += 4
                    # print(1, res)
                    if i and grid[i-1][j]:
                        res -= 2
                        # print(1, res)
                    if j and grid[i][j-1]:
                        res -= 2
                        # print(1, res)
        return res

s = Solution()
test = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
print(s.islandPerimeter(test))
test = [[1,0]]
print(s.islandPerimeter(test))