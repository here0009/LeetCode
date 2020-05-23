"""
Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

 

Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1
Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3
Example 5:

Input: grid = [[4]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
"""
from functools import lru_cache
class Solution:
    """
    not work
    """
    def minCost(self, grid) -> int:
        @lru_cache(None)
        def cost(i,j):
            print(i,j)
            if i > m or j > n:
                return float('inf')
            if i == m and j == n:
                return 0
            E,W,S,N = cost(i+1,j),cost(i-1,j),cost(i,j+1),cost(i,j-1)
            if grid[i][j] == 1:
                K = E
            elif grid[i][j] == 2:
                K = W
            elif grid[i][j] == 3:
                K = S
            elif grid[i][j] == 4:
                K = N
            return min(K,E+1,W+1,S+1,N+1)

        m,n = len(grid)-1, len(grid[0])-1
        return cost(0,0)


class Solution:
    def minCost(self, grid) -> int:
        """
        self.bfs save all the node we can go without change anything, then change the direction to the other 3 for each node in self.bfs, store the node we can traverse in an updated self.bfs. if target is reached, return the changes
        """
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def traverse(i,j,d):
            # print(i,j,d)
            visited[i][j] = 1
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            di,dj = directions[d-1]
            i += di
            j += dj
            if inRange(i,j) and not visited[i][j]:
                self.bfs.add((i,j))
                traverse(i,j,grid[i][j])
            

        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        changes = 0
        self.bfs = {(0,0)}
        traverse(0,0,grid[0][0])
        # print(self.bfs)
        while self.bfs:
            if (m-1,n-1) in self.bfs:
                return changes
            changes += 1
            bfs = {item for item in self.bfs}
            self.bfs = set()
            for i,j in bfs:
                for d in [1,2,3,4]:
                    if grid[i][j] != d: #change and traverse
                        traverse(i,j,d)
            # print(self.bfs)

from collections import deque
class Solution:
    def minCost(self, grid) -> int:
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        m, n = len(grid), len(grid[0])
        arrows = [(0,1),(0,-1),(1,0),(-1,0)]
        dp,costs = deque([(0,0,0)]),{}
        while dp:
            nx,ny,cost = dp.popleft()
            while inRange(nx,ny) and (nx,ny) not in costs: 
                costs[nx,ny] = cost
                dp += [(nx+dx,ny+dy,cost+1) for dx,dy in arrows if inRange(nx+dx,ny+dy)] #add nodes that could be reached if the direction is changed, first add then check
                dx,dy = arrows[grid[nx][ny]-1]
                nx,ny = nx+dx,ny+dy
            # print(costs)
            # print(dp)
        return costs[m-1,n-1]







S = Solution()
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(S.minCost(grid))

grid = [[1,1,3],[3,2,2],[1,1,4]]
print(S.minCost(grid))

grid = [[1,2],[4,3]]
print(S.minCost(grid))

grid = [[2,2,2],[2,2,2]]
print(S.minCost(grid))

grid = [[4]]
print(S.minCost(grid))
