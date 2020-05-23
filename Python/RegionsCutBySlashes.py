"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \\, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \\ is represented as "\\\\".)

Return the number of regions.



Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\\\/",
  "/\\\\"
]
Output: 4
Explanation: (Recall that because \\ characters are escaped, "\\\\/" refers to \\/, and "/\\\\" refers to /\\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\\\",
  "\\\\/"
]
Output: 5
Explanation: (Recall that because \\ characters are escaped, "/\\\\" refers to /\\, and "\\\\/" refers to \\/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\\', or ' '.
"""
"""
https://leetcode.com/contest/weekly-contest-115/problems/regions-cut-by-slashes/
"""
"""
Thoughts: use a 2*2 matrix to represnts gird[i], so / will  be [[0,1],[1,0]], \\ will be [[1,0],[1,0]]
"""
from collections import deque
class Solution_1:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        grid_Matrix = []
        N = len(grid)
        for i in range(N):
            grid_Matrix.extend([[],[],[]])
            for j in range(N):
                if grid[i][j] == '\\':          
                    grid_Matrix[3*i].extend([-1,0,0])
                    grid_Matrix[3*i+1].extend ([0,-1,0])
                    grid_Matrix[3*i+2].extend ([0,0,-1])
                elif grid[i][j] == '/':
                    grid_Matrix[3*i].extend([0,0,-1])
                    grid_Matrix[3*i+1].extend ([0,-1,0])
                    grid_Matrix[3*i+2].extend ([-1,0,0])
                else:
                    grid_Matrix[3*i].extend([0,0,0])
                    grid_Matrix[3*i+1].extend([0,0,0])
                    grid_Matrix[3*i+2].extend([0,0,0])
        
        print("###############")
        for row in grid_Matrix:
            print(row)
        d = deque()
        len_row = len(grid_Matrix)
        color = 0
        for row in range(len_row):
            for column in range(len_row):
                if grid_Matrix[row][column] == 0:
                    color += 1
                    d.append((row,column))
                    while d:
                        i,j = d.popleft()
                        # print(i,j)
                        grid_Matrix[i][j] = color
                        if i-1 >=0 and grid_Matrix[i-1][j] == 0:
                            d.append((i-1,j))
                        if i+1 < len_row and grid_Matrix[i+1][j] == 0:
                            d.append((i+1,j))
                        if j-1 >= 0 and grid_Matrix[i][j-1] == 0:
                            d.append((i,j-1))
                        if j+1 < len_row and grid_Matrix[i][j+1] == 0:
                            d.append((i,j+1))

        return color

class Solution:
    def dfs(self, matrix, i, j, color):
        if i>= 0 and i<len(matrix) and j>=0 and j<len(matrix) and matrix[i][j] == 0:
            matrix[i][j] = color
            self.dfs(matrix, i-1, j, color)
            self.dfs(matrix, i+1, j, color)
            self.dfs(matrix, i, j-1, color)
            self.dfs(matrix, i, j+1, color)

    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        grid_Matrix = []
        N = len(grid)
        for i in range(N):
            grid_Matrix.extend([[],[],[]])
            for j in range(N):
                if grid[i][j] == '\\':          
                    grid_Matrix[3*i].extend([-1,0,0])
                    grid_Matrix[3*i+1].extend ([0,-1,0])
                    grid_Matrix[3*i+2].extend ([0,0,-1])
                elif grid[i][j] == '/':
                    grid_Matrix[3*i].extend([0,0,-1])
                    grid_Matrix[3*i+1].extend ([0,-1,0])
                    grid_Matrix[3*i+2].extend ([-1,0,0])
                else:
                    grid_Matrix[3*i].extend([0,0,0])
                    grid_Matrix[3*i+1].extend([0,0,0])
                    grid_Matrix[3*i+2].extend([0,0,0])
        
        len_row = len(grid_Matrix)
        color = 0
        for row in range(len_row):
            for column in range(len_row):
                if grid_Matrix[row][column] == 0:
                    color += 1
                    self.dfs(grid_Matrix, row, column,color)               
        return color



s = Solution()
# print("grid 1")
# grid = [" /","/ "]
# for row in s.regionsBySlashes(grid):
#     print(row)
# print("grid 2")
# grid = [" /","  "]
# for row in s.regionsBySlashes(grid):
#     print(row)
# print("grid 3")
# grid = ["\\/","/\\"]
# for row in s.regionsBySlashes(grid):
#     print(row)
# print("grid 4")
# grid = ["/\\","\\/"]
# for row in s.regionsBySlashes(grid):
#     print(row)
# print("grid 5")
# grid = ["//","/ "]
# for row in s.regionsBySlashes(grid):
#     print(row)

grid = [" /","/ "]
print(s.regionsBySlashes(grid))

grid = [" /","  "]
print(s.regionsBySlashes(grid))

grid = ["\\/","/\\"]
print(s.regionsBySlashes(grid))

grid = ["/\\","\\/"]
print(s.regionsBySlashes(grid))

grid = ["//","/ "]
print(s.regionsBySlashes(grid))

grid = ["\\ \\\\/  ","\\\\ \\/\\ ","\\\\  \\ \\","\\\\ \\/\\/","\\\\\\ /  ","//// \\\\","\\\\\\/ //"]
print(s.regionsBySlashes(grid))