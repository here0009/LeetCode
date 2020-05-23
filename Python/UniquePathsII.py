"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
import copy
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        oppo_gird = copy.deepcopy(obstacleGrid)
        for i in range(row):
            for j in range(col):
                oppo_gird[i][j] = 1-obstacleGrid[i][j]

        blocked = False
        for i in range(col):
            if oppo_gird[0][i] == 0:
                blocked = True
            if blocked:
                oppo_gird[0][i] = 0

        blocked = False
        for j in range(row):
            if oppo_gird[j][0] == 0:
                blocked = True
            if blocked:
                oppo_gird[j][0] = 0

        # for line in oppo_gird:
        #     print(line)

        for i in range(1,row):
            for j in range(1,col):
                if oppo_gird[i][j] != 0:
                    oppo_gird[i][j] = oppo_gird[i-1][j] + oppo_gird[i][j-1]
                 
        return oppo_gird[row-1][col-1]

s = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0,0],[0,0,1],[0,1,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))

# obstacleGrid = [[0],[0]]
# print(s.uniquePathsWithObstacles(obstacleGrid))


obstacleGrid = [[1,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0],[1,1],[0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))