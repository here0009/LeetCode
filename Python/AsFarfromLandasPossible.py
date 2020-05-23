"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""
class Solution:
    def maxDistance(self, grid) -> int:
        def inRange(x,y):
            return 0 <= x < N and 0 <= y < N

        distance = -1
        N = len(grid)
        sumGrid = sum([sum(grid[i]) for i in range(N)])
        if sumGrid == 0 or sumGrid == N*N:
            return distance
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[0]*N for _ in range(N)]
        bfs = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    bfs.append((i,j))
                    visited[i][j] = 1
        while len(bfs) > 0:
            bfs_2 = []
            distance += 1
            for x,y in bfs:
                for dx,dy in directions:
                    tmp_x, tmp_y = x+dx, y+dy
                    if inRange(tmp_x,tmp_y) and not visited[tmp_x][tmp_y]:
                        visited[tmp_x][tmp_y] = 1
                        bfs_2.append((tmp_x,tmp_y))
            bfs = bfs_2
                
        return distance

s = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
print(s.maxDistance(grid))

grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(s.maxDistance(grid))

grid = [[0,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))