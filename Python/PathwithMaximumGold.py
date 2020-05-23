"""
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
class Solution:
    def getMaximumGold(self, grid) -> int:
        def inRange(i,j):
            return 0<=i<m and 0<=j<n

        def dfs(i,j):
            res = 0
            for di,dj in directions:
                tmpi,tmpj = i+di,j+dj
                if inRange(tmpi,tmpj) and not visited[tmpi][tmpj] and grid[tmpi][tmpj] != 0:
                    visited[tmpi][tmpj] = 1
                    res = max(res, dfs(tmpi, tmpj))
                    visited[tmpi][tmpj] = 0
            return res+grid[i][j]


        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = [[0]*n for _ in range(m)]
                    visited[i][j] = 1
                    res = max(res, dfs(i,j))
        return res

class Solution:
    """
    backtrack, the way it generate neighbors is good.
    """
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        # Given a row and a column, what are all the neighbours?
        def options(row, col):
            if row > 0:
                yield(row - 1, col)
            if col > 0:
                yield(row, col - 1)
            if row < len(grid) - 1:
                yield(row + 1, col)
            if col < len(grid[0]) - 1:
                yield(row, col + 1)
        
        # Keep track of current gold we have, and best we've seen.
        self.current_gold = 0
        self.maximum_gold = 0
        
        def backtrack(row, col):
        
            # If there is no gold in this cell, we're not allowed to continue.
            if grid[row][col] == 0:
                return
            
            # Keep track of this so we can put it back when we backtrack.
            gold_at_square = grid[row][col] 
            
            # Add the gold to the current amount we're holding.
            self.current_gold += gold_at_square
            
            # Check if we currently have the max we've seen.
            self.maximum_gold = max(self.maximum_gold, self.current_gold)
            
            # Take the gold out of the current square.
            grid[row][col] = 0
            
            # Consider all possible ways we could go from here.
            for neigh_row, neigh_col in options(row, col):
                # Recursively call backtrack to explore this way.
                backtrack(neigh_row, neigh_col)
            
            # Once we're done on this path, backtrack by putting gold back.
            self.current_gold -= gold_at_square
            grid[row][col] = gold_at_square 
        
        # Start the search from each valid starting location.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                backtrack(row, col)
        
        # Return the maximum we saw.
        return self.maximum_gold

s = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(s.getMaximumGold(grid))

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(s.getMaximumGold(grid))

grid = [[0]]
print(s.getMaximumGold(grid))

grid = [[1]]
print(s.getMaximumGold(grid))