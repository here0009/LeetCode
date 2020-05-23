"""
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 

Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
"""
import copy
class Solution_1:
    def colorBorder(self, grid, r0: int, c0: int, color: int):
        def valid(i,j):
            return i >= 0 and i < row and j >= 0 and j < col

        def dfs(i,j):
            if valid(i,j) and grid[i][j] == ori_color and (i,j) not in colored_gird:
                if i == 0 or i == row-1 or j==0 or j == col-1:
                    res_grid[i][j] = color
                for di,dj in adjacents:
                    if valid(i+di, j+dj) and grid[i+di][j+dj] != ori_color:
                        res_grid[i][j] = color
                colored_gird.add((i,j))
                for di,dj in adjacents:
                    dfs(i+di,j+dj)


        ori_color = grid[r0][c0]
        res_grid = copy.deepcopy(grid)
        row = len(grid)
        col = len(grid[0])
        colored_gird = set()
        adjacents = {(0,1),(0,-1),(1,0),(-1,0)}
        dfs(r0,c0)
        # grid[r0][c0] = ori_color
        return res_grid


class Solution:
    def colorBorder(self, grid, r0: int, c0: int, color: int):
        def valid(i,j):
            return i >= 0 and i < row and j >= 0 and j < col

        def dfs(i,j):
            if valid(i,j) and grid[i][j] == ori_color and (i,j) not in seen:
                seen.add((i,j))
                if i == 0 or i == row-1 or j==0 or j == col-1:
                    borders.add((i,j))
                for di,dj in adjacents:
                    dfs(i+di,j+dj)
                    if valid(i+di, j+dj) and grid[i+di][j+dj] != ori_color:
                        borders.add((i,j))

        ori_color = grid[r0][c0]
        row = len(grid)
        col = len(grid[0])
        seen = set()
        borders = set()
        adjacents = {(0,1),(0,-1),(1,0),(-1,0)}
        dfs(r0,c0)
        for i,j in borders:
            grid[i][j] = color
        return grid

s = Solution()
grid = [[1,1],[1,2]]
r0 = 0
c0 = 0
color = 3
print(s.colorBorder(grid, r0, c0, color))


grid = [[1,2,2],[2,3,2]]
r0 = 0
c0 = 1
color = 3
print(s.colorBorder(grid, r0, c0, color))


grid = [[1,1,1],[1,1,1],[1,1,1]]
r0 = 1
c0 = 1
color = 2
print(s.colorBorder(grid, r0, c0, color))


grid = [[1,2,1],[1,2,2],[2,2,1]]
r0 = 1
c0 = 1
color = 2
print(s.colorBorder(grid, r0, c0, color))

grid = [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]]
r0 = 1
c0 = 3
color = 1
print(s.colorBorder(grid, r0, c0, color))