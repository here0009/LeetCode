"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""
class Solution:
    def shortestPath(self, grid, k: int) -> int:
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def dfs(i,j,e,moves):
            if e < 0:
                return
            if moves >= self.res:
                return
            if (i,j,e) in moves_dict:
                return
            else:
                moves_dict[(i,j,e)] = moves
            if i == m-1 and j == n-1 and e >= 0:
                self.res = min(self.res, moves)
                return
            for dx,dy in directons:
                tmpx,tmpy = i+dx,j+dy
                if inRange(tmpx,tmpy):
                    if grid[tmpx][tmpy] == 1:
                        if e > 0:
                            dfs(tmpx,tmpy,e-1,moves+1)
                        else:
                            return
                    else:
                        dfs(tmpx,tmpy,e,moves+1)

        self.res = float('inf')
        m,n = len(grid), len(grid[0])
        directons = [(1,0),(0,1),(-1,0),(0,-1)]
        moves_dict = dict()
        dfs(0,0,k,0)
        if self.res == float('inf'):
            return -1
        else:
            return self.res

s = Solution()

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(s.shortestPath(grid,k))

grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
print(s.shortestPath(grid,k))


grid =[[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]]
k = 1
for row in grid:
    print(row)
print(s.shortestPath(grid,k))