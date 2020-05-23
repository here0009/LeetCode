"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
"""
class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Thoughts: 回溯法需要一个标记记录已经访问的节点, 完成访问后, 将标记还原.
        """
        
        def dfs(x, y, squares):
            if x < 0 or y < 0 or x >= row or y >= col:
                return
            if x == end[0] and y == end[1] and squares == empties:
                self.res += 1
                return
            if grid[x][y] != 0:
                return
            else:
                grid[x][y] = -2 #flag prevent to go back
                for d in directions: 
                    dfs(x+d[0], y+d[1], squares+1)
                grid[x][y] = 0 #revert, other paths can use grid[x][y] now.


        empties = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    empties += 1

        # print(start, end, empties)
        # print(grid)       
        self.res = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for d in directions:
            dfs(start[0]+d[0], start[1]+d[1], 0)
        return self.res

s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(s.uniquePathsIII(grid))

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(s.uniquePathsIII(grid))

grid = [[0,1],[2,0]]
print(s.uniquePathsIII(grid))
