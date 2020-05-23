"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        row = len(grid)
        col = len(grid[0])

        def remain_num(grid, num):
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == num:
                        return True
            return False

        mins = 0
        while True:
            plus_score = 0
            rotten_index = []
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        if i-1 >=0 and grid[i-1][j] == 1:
                            rotten_index.append((i-1,j))
                            plus_score += 1
                        if i+1 < row and grid[i+1][j] == 1:
                            rotten_index.append((i+1,j))
                            plus_score += 1
                        if j-1 >=0 and grid[i][j-1] == 1:
                            rotten_index.append((i,j-1))
                            plus_score += 1
                        if j+1 < col and grid[i][j+1] == 1:
                            rotten_index.append((i,j+1))
                            plus_score += 1

            for i, j in rotten_index:
                grid[i][j] = 2

            if plus_score == 0:
                if remain_num(grid,1):
                    return -1
                else:
                    break
            else:
                mins += 1
        return mins

s = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(s.orangesRotting(grid))

grid = [[0,2]]
print(s.orangesRotting(grid))