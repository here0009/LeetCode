"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]
Output: 2
Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        def isValid(i,j):
            return i >= 0 and i < N and j >= 0 and j < N and grid[i][j] == 0


        N = len(grid)
        if N == 1:
            return int(grid[0][0] == 0)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        visted = {(0,0)}
        stack = [(0,0)]
        layers = 1
        while stack:
            stack_2 = []
            layers += 1
            for x,y in stack:
                for dx, dy in directions:
                    tmp = x+dx, y+dy
                    if tmp == (N-1, N-1):
                        return layers
                    if tmp not in visted and isValid(tmp[0],tmp[1]):
                        stack_2.append(tmp)
                    visted.add(tmp)
            # print(stack_2)
            # print(visted)
            stack = stack_2
        return -1


s = Solution()
grid = [[0,1],[1,0]]
print(s.shortestPathBinaryMatrix(grid))

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(s.shortestPathBinaryMatrix(grid))

grid = [[1]]
print(s.shortestPathBinaryMatrix(grid))

grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
print(s.shortestPathBinaryMatrix(grid))